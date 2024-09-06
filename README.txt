Name: Matthew Von Nathaniel E. Corcuera
Activity: Software Automation Engineer Assessment

====================================================
Commands to run scripts 5 times and generate html reports:

1. Edit a Kanban Card
pytest test_complete_task.py --count 5 --html=test_complete_task_report.html

2. Delete a Kanban Card
pytest test_delete_kanban.py --count 5 --html=test_delete_kanban_report.html

3. Toggle dark mode
pytest test_toggle_dark_mode.py --count 5 --html=test_toggle_dark_mode_report.html