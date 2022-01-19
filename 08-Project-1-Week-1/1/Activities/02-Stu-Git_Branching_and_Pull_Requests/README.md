# Git Branching and Pull Requests


In this activity, we will create a new branch, implement a feature, and then submit a pull request back to the main branch. We will also review pull requests and how to merge them into main.


## Instructions

The instructions are divided into two parts. In Part 1, you’ll create a branch and submit a pull request. In Part 2, you’ll review and approve a pull request.

### Part 1: Create a Branch and Submit a Pull Request

In this section, you will create a branch, add a feature, and submit a pull request. Only ONE group member should complete this section. That group member should share their screen so the other members of the group can observe the process.

1. Clone the project repository onto your computer and `cd` into it.

2. Run the following command in your terminal to create and checkout to a new branch:

  ```shell
  git checkout -b add-stock-data
  ```

3. You should now be on a new branch named "add-stock-data." In order to verify that this process worked, run the following command in your terminal:

  ```shell
  git branch
  ```

4. You should see two branches listed: `main` and `add-stock-data.` The `add-stock-data` branch should have an asterisk to its left, indicating that you're currently on this branch.

5. Open this repository in Visual Studio Code. In the repository folder, create a new file named `stocks.py`. Inside this file, add the following code snippet to define and call a basic Python function. Save the file.

  ```python
  def stocks(stock1, stock2):
      sum = stock1 + stock2
      return sum

  sum = stocks(45.23, 187.56)
  print(f"The total value of the two stocks is {sum}.")
  ```

6. In your terminal, add and commit the changes. Then push your code up by running the following command in your terminal:

  ```shell
  git push origin add-stock-data
  ```

This should push your code up to a GitHub branch of the same name (“add-stock-data”).

7. Go to the main repository page on GitHub. You should see a message confirming that you have just made a commit to the repository.

8. Click the button "Compare & pull request."

9. On the following screen, add a description of the work completed and click the "Pull Request" button.

10.  If completed successfully, you should see the pull request listed under the repository's "Pull request" tab.

### Part 2: Review and Approve a Pull Request

In this section, you will review the pull request from Part 1 and merge it into the main branch. A different project member should complete this section. That member should share their screen so that the other project members can observe.

1. Clone the repository to your computer if you haven't already, and `cd` into it.

2. Test the changes introduced by the `add-stock-data` branch locally. In order to examine the new branch on your local machine, run the following commands in your terminal. This code should bring the copy of the `add-stock-data` branch that's on GitHub onto your computer:

  ```shell
  git fetch
  ```

  ```shell
  git checkout -b add-stock-data origin/add-stock-data
  ```

3. Confirm that you are in the `add-stock-data` branch by running the following in your terminal:

  ```shell
  git branch
  ```

You should see two branches listed: `main` and `add-stock-data`. The branch `add-stock-data` will have an asterisk by its name, indicating that you are checked into the `add-stock-data` branch.

4. Open Visual Studio code by typing `code .` in your terminal. Confirm that there's a `stocks.py` file in your local repository. Run the code to make sure everything works properly.

5. Once the code is confirmed, you can check out to your local `main` branch by running the following in your terminal:

  ```shell
  git checkout main
  ```

6. Return to your GitHub repository's main page and go to the "Pull request" section. Select the `add-stock-data` pull request from the list.


7. On the next page, select the option to see "Files changed."

8. You should be presented with all of the files changed in this pull request, specifically `stocks.py`.

9. If there were any changes you would like to make, you would click the line number to leave a comment. The pull request author would see it and have to address it before approval. In this case, click "Review changes" and approve the pull request.

10. Click the "Merge pull request" button to add the branch's changes into the main branch.

11. Once the changes have been merged, navigate back to your terminal and `cd` into the local repository for the project, though you will likely already be there from completing the prior steps. You can delete the feature branch from your machine by running the following in your terminal:

  ```shell
  git branch -D add-stock-data
  ```

Confirm that the branch was deleted by running the following command:

  ```shell
  git branch
  ```

Only the `main` branch should be listed. It should be labeled with an asterisk, confirming that you are checked into the `main` branch.

12. Finally, use `git pull` on your `main` branch to update it. Navigating back to Visual Studio Code, you should now see the `stocks.py` file included in your main branch.

  ```shell
  git pull
  ```

---

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
