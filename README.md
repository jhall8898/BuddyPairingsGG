## How to use:

It's pretty simple to use, just download the folder and open EmailAutomation.py in whatever IDE you want, I like to use [Thonny](https://thonny.org/) for Python because it's ridiculously easy to use and doesn't really require any set-up.
<br /><br />
You will see three fields that need to be filled in: toList, email_sender, email_password. 
<br /><br />
Make sure you move the file you want the program to read into the same folder that you downloaded earlier. To quickly locate the path for your file, simply open your computer's terminal and [drag the file into your terminal](https://ostechnix.com/drag-and-drop-files-and-folders-in-terminal-to-print-their-absolute-path/). As far as I know, this works with all operating systems. This will give you the most accurate path to your file. You can then copy that path into `toList = buddyPairing('Insert File Name')`. 
<br /><br />
**This program only accepts excel files, please make sure you label the columns appropriately. Required column labels are as follows (do not include single quotation marks in column labels): 'Email', 'Experience', 'Time', 'Level', 'Interest', 'Date'. For reference, experience refers to the type of exercise the user has experience in, interest is what the user wants to do with their buddy, level refers to experience level.** 
<br /><br />
Make sure 2-step verification is enabled for your email account (Google-based) so that you can create an [app-specific password](https://support.google.com/mail/answer/185833?hl=en) to use in the program.
Once that's done, all you need to do is to fill in `email_sender = 'Insert Sender Email'` with your email and `email_password = 'Insert Sender Email Password'` with the password generated from the app-specific password and run the code. Please note that the email you put for email_sender will be visible to recipients.
<br /><br />
## Disclaimer:
A copy of the form we sent to participants can be found [here](https://docs.google.com/forms/d/1ZHVmdJOoLvg0yr5K2UwEOlvRc0cX3hT8jqW88aV3UDg/edit)
<br /><br />
This was a rushed project so there may be a few errors, as far as I know, the code still works. I might come back and update it as necessary.
