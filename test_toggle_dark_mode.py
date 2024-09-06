from playwright.sync_api import Playwright, sync_playwright, expect

def test_toggle_dark_mode(playwright: Playwright) -> None:
	browser = playwright.chromium.launch(headless=False, slow_mo=1000)
	context = browser.new_context()
	page = context.new_page()
	page.set_viewport_size({"width": 800, "height": 600})
	
	#Set up toggle paths
	togglePath1 = page.locator('xpath=//*[@id="app"]/main/div[1]/div[1]/div/div[3]/div[1]/label')
	togglePath2 = page.locator('xpath=//*[@id="app"]/main/div[1]/div[1]/div/div[4]/div[1]/label')
	togglePath3 = page.locator('xpath=//*[@id="app"]/main/div[1]/div[1]/div/div[5]/div[1]/label')
	togglePath4 = page.locator('xpath=//*[@id="app"]/main/div[1]/div[1]/div/div[6]/div[1]/label')
	
	#Open Kanban Application
	page.goto("https://kanban-566d8.firebaseapp.com/task1725532251709task1725532259561task1725532275940task1725532304478task1725532307861task1725532328050task1725532335693task1725532353265")
	
	#Toggle Dark Mode	
	if(togglePath1.is_visible()):
		togglePath1.click()
	elif(togglePath2.is_visible()):
		togglePath2.click()
	elif(togglePath3.is_visible()):
		togglePath3.click()
	else:
		togglePath4.click()
		
	print("Dark mode has been toggled")
	
	#Verify that dark mode is enabled (Color has changed)
	expect(page.locator('xpath=//*[@id="app"]/header/div[2]')).to_have_css("scrollbar-color", "rgb(99, 95, 199) rgb(43, 44, 55)")
	
	context.close()
	browser.close()

with sync_playwright() as p:
    test_toggle_dark_mode(p)