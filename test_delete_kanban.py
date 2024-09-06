from playwright.sync_api import Playwright, sync_playwright, expect

def test_delete_kanban(playwright: Playwright) -> None:
	browser = playwright.chromium.launch(headless=False, slow_mo=1000)
	context = browser.new_context()
	page = context.new_page()
	
	#Open Kanban Application
	page.goto("https://kanban-566d8.firebaseapp.com/task1725532251709task1725532259561task1725532275940task1725532304478task1725532307861task1725532328050task1725532335693task1725532353265")
	
	#Add new task - to ensure that there will always be a task in the second column
	page.get_by_role("button", name="+ Add New Task").click()
	page.locator('xpath=//*[@id="Title"]').fill("Sample Task")
	page.get_by_label("Description").fill("Sample Description")
	page.locator('xpath=//*[@id="app"]/div[2]/form/div/div[4]/div[1]/div[1]/input').fill("Subtask 1")
	page.locator('xpath=//*[@id="app"]/div[2]/form/div/div[4]/div[2]/div[1]/input').fill("Subtask 2")
	page.locator('xpath=//*[@id="app"]/div[2]/form/div/div[5]/div').click()
	page.locator('xpath=//*[@id="app"]/div[2]/form/div/div[5]/div/div[3]/div[2]').click()
	page.get_by_role("button", name="Create Task").click()
	
	#Click Kanban Card
	page.locator('xpath=//*[@id="app"]/main/div[1]/div[2]/div/div/div[1]/section[2]/div[2]/article[1]').click()
	task = page.locator('xpath=//*[@id="app"]/div[2]/div/div/div[1]/h4').text_content()
	print("{} card has been clicked".format(task))
	
	#Click Ellipsis Button
	page.locator('xpath=//*[@id="app"]/div[2]/div/div/div[1]/div/div[1]').click()
	print("Ellipsis button has been clicked")
	
	#Click Delete Task
	page.locator('xpath=//*[@id="app"]/div[2]/div/div/div[1]/div/div[2]/div/p[2]').click()
	print("Delete task button has been clicked")
	
	#Confirm Deletion
	page.get_by_role("button", name="Delete").click()
	print("Task has been confirmed for deletion")
	
	#Verify that the deleted task is no longer present
	expect(page.get_by_text(task)).not_to_be_visible()
	print("Task is no longer visible")
	
	context.close()
	browser.close()

with sync_playwright() as p:
    test_delete_kanban(p)
	
	