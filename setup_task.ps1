$action = New-ScheduledTaskAction -Execute 'C:\Users\Gaming\AppData\Local\Programs\Python\Python312\python.exe' -Argument 'c:\Users\Gaming\GitHubProject\auto-commits\repos\Sounds\update_questions.py' -WorkingDirectory 'c:\Users\Gaming\GitHubProject\auto-commits\repos\Sounds'
$trigger = New-ScheduledTaskTrigger -Daily -At '8:00AM'
Register-ScheduledTask -TaskName 'DailyQuizUpdate' -Action $action -Trigger $trigger -Description 'Generates 5 new AI quiz questions daily and commits to git'
Write-Host 'Scheduled task "DailyQuizUpdate" created successfully! It will run daily at 8:00 AM.'
