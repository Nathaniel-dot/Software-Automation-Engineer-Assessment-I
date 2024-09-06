from playwright.sync_api import Playwright, sync_playwright, expect

def test_complete_task(playwright: Playwright) -> None:
	browser = playwright.chromium.launch(headless=False, slow_mo=1000)
	context = browser.new_context()
	page = context.new_page()
	
	#Open Kanban Application
	page.goto("https://kanban-566d8.firebaseapp.com/task1725532251709task1725532259561task1725532275940task1725532304478task1725532307861task1725532328050task1725532335693task1725532353265")
	
	#Get count of tasks in the first column
	firstColumnCount = page.locator('xpath=//*[@id="app"]/main/div[1]/div[2]/div/div/div[1]/section[1]/div[2]').get_by_role("article").count()
	
	#Add new task - to ensure that there will always be a task in the second column
	page.get_by_role("button", name="+ Add New Task").click()
	page.locator('xpath=//*[@id="Title"]').fill("Sample Task")
	page.get_by_label("Description").fill("Sample Description")
	page.locator('xpath=//*[@id="app"]/div[2]/form/div/div[4]/div[1]/div[1]/input').fill("Subtask 1")
	page.locator('xpath=//*[@id="app"]/div[2]/form/div/div[4]/div[2]/div[1]/input').fill("Subtask 2")
	page.locator('xpath=//*[@id="app"]/div[2]/form/div/div[5]/div').click()
	page.locator('xpath=//*[@id="app"]/div[2]/form/div/div[5]/div/div[3]/div[2]').click()
	page.get_by_role("button", name="Create Task").click()
	
	#Complete subtasks
	page.get_by_text("Sample Task").click()
	page.locator('xpath=//*[@id="app"]/div[2]/div/div/div[2]/div/label[1]').click()
	page.locator('xpath=//*[@id="app"]/div[2]/div/div/div[2]/div/label[2]').click()
	
	#Verify that the subtask is striked through
	expect(page.locator('xpath=//*[@id="app"]/div[2]/div/div/div[2]/div/label[1]/span')).to_have_css("text-decoration-line", "line-through")
	expect(page.locator('xpath=//*[@id="app"]/div[2]/div/div/div[2]/div/label[2]/span')).to_have_css("text-decoration-line", "line-through")

	#Verify the number of completed subtasks is correct
	expect(page.locator('xpath=//*[@id="app"]/div[2]/div/div/div[2]/p')).to_contain_text("2 of 2")
	
	#Move Kanban card to first column
	page.locator('xpath=//*[@id="app"]/div[2]/div/div/div[3]/div').click()
	page.locator('xpath=//*[@id="app"]/div[2]/div/div/div[3]/div/div[3]/div[1]').click()
	
	#Verify that the kanban card is moved to the first column (Count should have been incremented by one)
	expect(page.locator('xpath=//*[@id="app"]/main/div[1]/div[2]/div/div/div[1]/section[1]/div[2]').get_by_role("article")).to_have_count(firstColumnCount + 1)
	
	context.close()
	browser.close()

with sync_playwright() as p:
    test_complete_task(p)
	
	