# Module 2: Virtual Class II Lesson Plan (2 hours)

## Overview

In today's lesson, students will get a taste of both hard and soft everyday skills that they'll use throughout their careers, like gathering and expressing software requirements, converting requirements to code, and uploading and documenting their work to GitHub.

## Learning Objectives

By the end of this lesson, students will be able to do the following:

* Build a command line interface (CLI) using Python Fire and Questionary.

* Create and manage GitHub repositories via the command line.

* Organize and document a project in GitHub using a `README.md` file.

---

## Time Tracker

| Start  | #  | Activity Name                                  | Duration |
|---     |--- |---                                             |---       |
| 7:00PM | 1  | Instructor Do: Welcome and Check-In              | 0:05     |
| 7:05PM | 2  | Instructor Do: Usability and the CLI             | 0:15     |
| 7:20PM | 3  | Instructor Do: ATM Application                 | 0:10     |
| 7:30PM | 4  | Student Do: Build ATM Functions                | 0:20     |
| 7:50PM | 5  | Instructor Review: Build ATM Functions         | 0:10     |
| 8:00PM | 6  | Instructor Do: Version Control                 | 0:10     |
| 8:10PM | 7  | Student Do: Create a GitHub Repository         | 0:15     |
| 8:25PM | 8  | Instructor Review: Create a GitHub Repository  | 0:05     |
| 8:30PM | 9  | Instructor Do: Documentation                   | 0:10     |
| 8:40PM | 10  | Student Do: Explore README.md Files                  | 0:10     |
| 8:50PM | 11  | Instructor Review: Explore README.md Files          | 0:05     |
| 8:55PM | 12 | Recap                                          | 0:05     |
| 9:00PM | 13 | End                                            |          |

---


## Instructor Do: Office Hours (0:30)

Welcome to Office Hours! Remind the students that this is their time to ask questions and get assistance from their instructional staff as they learn new concepts and work on the Challenge assignment. Feel free to put students in groups to focus on specific topics, or to have 1:1s with students.

Expect that students may ask for assistance such as the following:

* Challenge assignment
* Further review on a particular subject
* Debugging assistance
* Help with computer issues
* Guidance with a particular tool

---

## Class Activities

### 1. Instructor Do: Welcome Students and Student Check-In (5 min)

Welcome everyone to class, and ask the students how they feel about the Module 2 material so far:

* How confident are you in explaining the aspects of software engineering that we’ve covered so far? What topics do you find most interesting?

Tell the students that the material covered in this lesson will help them complete the Challenge assignment. There will be time at the end of class for a Challenge Q&A.

### 2. Instructor Do: Usability and the CLI (15 min)

In this section, you will discuss the concepts of **usability** as they relate to developing a program.

* In the context of software engineering, **usability** is how effectively and efficiently a user can perform tasks within an application.

Ask the students the following question:

* As you review the ATM application, what do you think will make the application more usable? In particular, consider the Python libraries we’ve used in this module, like Fire and Questionary.

Guide students toward the following concepts:

  * A **command-line interface**, or CLI, can be developed—enabled by the Python Fire library and used in conjunction with the Questionary library.

  * **CLI integration** for the ATM should clearly define all of the menu options that the user can select.

  * **Error messaging** improves the user experience when the reason for errors is clearly and quickly displayed.

  * **System exit** functions terminate the program whenever there is an error, rather than leaving a user in limbo. While terminating the program this way is better than having the program break, it would be more user-friendly if the user was able to return to the previous step of the program to fix the mistake.

End the discussion about usability by touching on the following points:

  * Designing an application with usability in mind is no small task. Companies have entire teams devoted to designing for usability and the user experience.

  * Fintech companies, which by definition use technology as a delivery platform, spend billions creating programs that use the characteristics we just discussed in order to engage and simplify a user’s interaction with their application.

  * Designing for usability is important because you can draw direct links between application usability, customer satisfaction, and increased revenue.

Ask if students have any questions before moving on.

---

### 3. Instructor Do: ATM Application (10 min)

**Files:**

[ATM Application](Activities/01_Ins_ATM_Application/Solved/atm)

[requirements.txt](Activities/01_Ins_ATM_Application/Solved/atm/requirements.txt)

[accounts.csv](Activities/01_Ins_ATM_Application/Solved/atm/data/accounts.csv)

In this section, you'll review how to build the ATM application functionality, focusing on the usability aspects that have already been integrated.

Let students know that the modularized code from the first virtual class has been upgraded with new features based on the user stories and usability.

Explain that the preliminary versions of the ATM application come with a `requirements.txt` file. Open this file and review the Python libraries that will be used, as shown in the following code:

```code
fire==0.3.1
questionary==1.5.2
```

* A `requirements.txt` file helps to ensure that users of your application will run the same versions of the necessary libraries that developers used in their virtual environments.

Tell the students that they’ll need to set up a new virtual environment called `atmdev` because specific versions of certain libraries are required. They'll do this on their on in the next activity, so for now simply walk them through the commands.

Create a new conda environment with the following command:

  ```shell
  conda create -n atmdev python=3.7 anaconda
  ```

Activate the new dev environment with the following command:

  ```shell
  conda activate atmdev
  ```

Next, navigate to the root of the folder that houses your ATM files and install `requirement.txt`. Explain to the students that it’s installing the specific versions of the libraries that the application developers require. The code should appear as follows:

  ```shell
  pip install -r requirements.txt
  ```

Finally, open `atm.py` in the `Solved` folder and review the functions provided.

* Start with `name/main`, which initiates the CLI with the `run` function. Explain that the `Fire` library enables the command-line interface for the application. The function looks like this:

  ```python
  if __name__ == "__main__":
      fire.Fire(run)
  ```

Review the steps of the `run` function and explain to students how they relate to the rest of the application.

Tie the following steps back to user stories and system requirements:

  * `login` initiates the user login by asking for a PIN. (This piece connects to a user story.)

  * The `validate_pin` function is imported from the [utils module](Activities/01_Ins_ATM_Application/Solved/atm/utils.py), which you can open and show.

    * PIN validation triggers the `load_accounts` function, also stored in the utils module, which reads the `account.csv` file. Show students the `account.csv` file that contains the PIN number and account balances.

    * The user PIN is checked against the account list. If there’s a match, the account gets returned. If there’s no match, the system exits with an error message.

  * The next step in the `run` function is `main_menu`, which asks an approved user what action they would like to take: check balance, make a deposit, or make a withdrawal. (This piece connects to a user story.)

  * Back in `run`, the chosen action triggers one of the following three events:

    * `check balance` just returns the balance and exits.

    * `make_deposit` initiates the deposit function, in which a deposit amount is asked for and checked, the balance is adjusted, and the account is returned. (This piece connects to a user story.)

    * `make_withdrawal` has the actions defined but still needs to be coded. (This piece connects to a user story and two system requirements.)

  * Finally, a print statement confirms both the action and the adjusted balance.

Ask the students if they have any questions about the code. Let them know that they’ll have to fill in the code for the `validate_pin` and `make_withdrawal` functions in the next activity.

---

### 4. Student Do: Build ATM Functions (20 min)

In this activity, students will complete the two missing functions highlighted in the ATM application code review: `validate_pin` and `make_withdrawal`.

The function definitions have been written; their job is to complete the code that allows the function to perform the specified action.

**Files:**

[Instructions](Activities/02_Stu_Build_ATM_Functions/README.md)

[ATM Application](Activities/02_Stu_Build_ATM_Functions/Unsolved/atm/atm.py)

[requirements.txt](Activities/02_Stu_Build_ATM_Functions/Unsolved/atm/requirements.txt)

[Resources/accounts.csv](Activities/02_Stu_Build_ATM_Functions/Unsolved/atm/data/accounts.csv)

Summarize for students their task in this activity:

* Based on the user stories, we designed an initial version of an ATM application in a single Python script. In this activity, you'll work in teams to complete the function body for `validate_pin` and both the docstring and the function body for the `make_withdrawal` function.

Display the following image of a multiline docstring and briefly review the concept:

* **Docstrings** in Python use the `"""` triple-quotation character to define multiline comments and describe the purpose of the function, the parameters and their required data types, and the returning output and its data type.

* The function should resemble the following code:

```python
def example_function(arg1, arg2):
     """Example function description.

    Args:
    arg1 (int): Description of arg1.
    arg2 (int): Description of arg2.

    Returns:
    output (int): Description of return value.
    """
    function body
    return output
```

**Instructions:**

1. Create a new development environment called `atmdev` and install the libraries contained in the `requirements.txt` file.

  * From your terminal instance, create a new virtual environment called `atmdev`, using the following code:

    ```code
    conda create -n atmdev python=3.7 anaconda
    ```

  * Activate the new `atmdev` environment as follows:

    ```code
    conda activate atmdev
    ```

  * Navigate to the root of this activity folder and install the provided `requirements.txt` using the following code:

    ```code
    pip install -r requirements.txt
    ```

2. Open [`atm.py`](Activities/02_Stu_Build_ATM_Functions/Unsolved/atm/atm.py) and review the Python script. Then open [`utils.py`](atm/utils.py) and [`make_withdrawal.py`](Activities/02_Stu_Build_ATM_Functions/Unsolved/atm/actions/make_withdrawal.py). You'll be completing the following functions:

  * `verify_pin(pin)`, located in the utils module

    * Verify that the length of the pin is six characters.

      * If true, print a validation message and return `True`.

      * If false, then return `False`.

  * `make_withdrawal(account)`, located in the actions folder

    * Use `make_deposit(account)` as a guide.

    * Complete the docstring using the docstring from `make_deposit(account)` as a guide.

    * Use the Questionary library to ask the user how much they want to deposit. Set the return equal to the variable `amount`. Make sure that `amount` is a floating point value.

    * If `amount` is less than or equal to 0.0, exit the system with an error message indicating that it’s not a valid withdrawal amount.

    * Validate that `amount` is less than or equal to `account["balance"]`.

      * If the amount is valid, adjust the `account["balance"]` for the withdrawal, and print a confirmation message and return the adjusted account.

      * If the amount isn't valid, exit the system with an error message that tells the user that they don't have enough money in the account to cover the withdrawal.

3. Run your application!

**Bonus:** If you have time, try writing the accounts, including the one that has been adjusted, back to the CSV file.

---

### 5. Instructor Review: Build ATM Functions (10 min)

**Files:**

[ATM Application](Activities/02_Stu_Build_ATM_Functions/Solved/atm/atm.py)

[requirements.txt](Activities/02_Stu_Build_ATM_Functions/Solved/atm/requirements.txt)

[Resources/accounts.csv](Activities/02_Stu_Build_ATM_Functions/Solved/Resources/accounts.csv)

In this part of the lesson, review the steps associated with the “Build ATM Functions” activity.

First, ask students if they had any trouble creating the new dev environment.

Then, ensure that students know they need to be in the root folder of the project to install the libraries contained in the `requirements.txt` file.

* The code for the `validate_pin(pin)` function is as follows:

  ```python
  def validate_pin(pin):
      """Verifies that PIN is 6 digits long."""

      # Verifies length of pin is 6 digits, else return False.
      if len(pin) == 6:
          print(f"Your PIN is valid")
          return True
      else:
          return False
  ```

* The code for the `make_withdrawal(account)` function, including the docstring, is as follows:

  ```python
  def make_withdrawal(account):
    """Withdrawal Dialog.

        This application captures the withdrawal amount from the user,
        validates the amount, that their are enough funds in the account,
        adjusts the account balance for the withdrawal and returns the adjusted account.

        Args:
            account(dict): user account information including pin and balance.

        Return:
            account(dict): user account with balance adjusted for deposit

    """
    # Use questionary to capture the withdrawal and set equal to amount variable. Be sure to set amount as a floating point number.
    amount = questionary.text("How much would you like to withdraw?").ask()
    amount = float(amount)

    # Validates amount of withdrawal. If less than or equal to 0 system exits with error message.
    if amount <= 0.0:
        sys.exit("This is not a valid withdrawal amount. Please try again.")

    # Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
    # Else system exits with error messages indicating that the account is short of funds.
    if amount <= account["balance"]:
        account["balance"] = account["balance"] - amount
        print("Your withdrawal was successful!")
        return account
    else:
        sys.exit(
            "You do not have enough money in your account to make this withdrawal. Please try again."
        )
  ```

Demonstrate to students how to initiate the `atmdev` environment, install `requirements.txt`, and run the solved `app.py`.

Tell students that now that the ATM app is working, we’ll switch gears to discuss Version Control.

---

### 6. Instructor Do: Version Control (10 min)

In this section, you will discuss the importance of version control in the process of software development.

Start by asking students questions about their own experiences with version control.

* How did you collaborate with others?

* How did you manage changes to your work?

Then, transition to talking about Git and GitHub. Ask students the following questions:

* Did you use GitHub before beginning this boot camp?

* If so, how has your usage changed? If not, how has your experience with it been so far?

Discuss your professional experiences using Git and GitHub. Share any stories you have about workflows that you have used in the past, preferences for using Git and GitHub, and what you have personally found to be best practices.

**Note:** If there are advanced students who have used Git and GitHub or other version control systems professionally, ask them to share their best practices.

Finally, discuss why using Git via the command line, or terminal, is important. Although it’s perfectly fine to manage Git via the GUI or app, this is not always possible. Cloud platforms require using Git through the terminal, so it's best practice to start doing that now.

Ask the students if they were able to use Git via the command line and if they experienced any issues. Ask if they have any questions before moving on.

---

### 7. Student Do: Create a GitHub Repository (15 min)

**Files:**

[Instructions](Activities/03_Stu_Create_Github_Repository/README.md)

In this activity, students will get some additional practice creating a repository via the terminal. Tell students they will do the following:

* Create a repository for the ATM application, including a `README.md` file that follows the [template](Activities/03_Stu_Create_Github_Repository/Template/README_Template.md) provided in the activity files.

* Use only terminal commands in order to do this; don’t use the GUI or VS Code.

**Instructions:**

1. Create the Repository

    * Create a GitHub repository with a name that describes your ATM application.

    * Initialize your repository with a `README.md` file.

    * Once your repository is created, click the green "Code" button and copy the https clone link.

2. Clone the Repository

    * Open a terminal window and use `cd` commands to navigate to the directory where you would like to save your repository.

    * Use the `git clone` command and the link you copied previously to clone the repository in the location you selected.

3. Add and Edit Files

    * Copy the files for your ATM application into this folder.

    * Edit your `README.md` file so that the headers match the [README template](Activities/03_Stu_Create_Github_Repository/README.md).

    * Fill in the sections of the `README.md` file with brief descriptions.

4. Stage and Commit Changes

    * Use the `git status` and `git add` commands to review the changes you have made and track your new files.

    * Once you have tracked your files using `git add`, commit these changes with a message using `git commit -m` followed by a short but descriptive summary of what you changed.

5. Push Local Changes to Remote Repository

    * Use the `git push` command to copy your local changes to the GitHub remote repository.

    * Go to your Github repository to see your changes.

---

### 8. Instructor Review: Create a GitHub Repository (5 min)

In this section, review the previous activity. Specifically, do the following:

* Confirm that all of the students were able to create their repository and stage and commit changes via the terminal.

* Ask students how comfortable they feel managing changes via the terminal.

* Encourage students to keep practicing this skill until it becomes second nature.

---

### 9. Instructor Do: Documentation (10 min)

In this section, you will discuss the importance of documenting projects with readme files and comments.

Start this discussion by sharing a story from your professional experience that relates to project documentation.

* For example, think of a time you had to work on a project that someone else had started. Maybe their documentation was exceptional, which was helpful, or maybe it was poor, and that set you back.

Next, ask the students to talk about their experiences with documentation.

* Have they used repos created by other people? If so, what was helpful about it, and what was challenging?

Discuss the importance of making applications that can be used by others. Be sure to mention the role this plays in getting a job (e.g., employers can review your GitHub repository to get a sense of your skills, experience, and projects).

---

### 10. Student Do: Explore README.md Files (10 min)

**Files:**

[Instructions](Activities/04_Stu_Explore_ReadMes/README.md)

In this activity, students will work in groups to review `README.md` files for two GitHub repos, and then share suggestions for making them easier to read and understand.

**Instructions:**

1. Go to the [trending page](https://github.com/trending?spoken_language_code=en) on GitHub and choose a repository to explore. Pick something that interests you and your team.

2. Review the `README.md` file and discuss the following with your group:

    * What do you like about this readme?

    * What do you not like?

    * Is there anything you find confusing?

3. As you explore the readme file, consider the following:

    * Does the text of the readme make you excited to learn more about the project?

    * Is it clear who the intended audience is?

    * Does the readme provide enough information?

    * Does it provide too much information?

4. After you have discussed the readme file with your group, pick a second repository and then compare the two readme files.

---

### 11. Instructor Review: Explore README.md Files (5 min)

Ask each group to share something helpful that they saw in a readme file, as well as something that they felt could be improved.

---

### 12. Recap (5 min)

Recap today's lesson for the students:

* Part of today's lesson focused on version control and collaboration using Git and GitHub via the terminal. Working in the fintech industry usually involves team collaboration on complex projects, so building good habits with Git and GitHub now will be very helpful for you as you advance in your work.

* Documentation is also an important, if not always glamorous, part of software development. Good documentation can inspire others to read and use your work. It's also a critical part of building interesting and complex projects that are worth using.

* Ask the students if they have any questions about today's lesson.

* Thank the students for their time and attention. Let them know that any remaining time will be used for open office hours.

---

## Open Office Hours

Announce office hours. Invite students to stay on the Zoom and start the Challenge assignment while they have live support from instructional staff.

#### Q&A and System Support

This is an opportunity to support students in any way that they need.

* Ask the students if they have any questions about the material covered in today's virtual class.

* Ask the students if they have any questions about the material covered in the async content.

* Review the Challenge assignment with the students and remind them that this assignment is due on Sunday evening.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
