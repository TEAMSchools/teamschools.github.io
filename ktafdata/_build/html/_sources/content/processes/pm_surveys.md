# Performance Management and Surveys

## Surveys

### Set Up

1. Create a new survey on [Alchemer (formerly SurveyGizmo)](https://www.alchemer.com).

2. Create Name question for the survey taker
    * Under Logic, alias it as “respondant_df_employee_number”
    ![](images/survey_setup_1.png)
    * If piping from Survey HQ, create a default answer with a URL parameter (best practice is to match the Alias and the parameter)

3. Create any additional piping/logic questions (see examples below). Be sure to add aliases and default answers. You can hide questions as needed under Logic -> Hide Question By Default
    ![](images/survey_setup_2.png)
    ![](images/survey_setup_3.png)

4. Continue creating questions and setting up the survey. Be sure to alias each question.

5. When done, go to Style -> Themes -> Your Theme Library and apply the KTAF survey theme
    ![](images/survey_setup_4.png)

6. Under Share, create a new campaign (outlined below).

7. The survey will now be ready to flow into [gabby](content/databases/gabby.md). You’ll need to adjust views and create an output view. Additionally, if you want to create question options (eg: Plug in a list of all active staff members), you’ll need to adjust the questions_options tool. For questions where you’re updating question options, be sure to set the options to alphabetical under Layout.
    ![](images/survey_setup_5.png)

---

### Self & Others + Manager Assignments on the PM Management Document

#### Background
* School Leaders and DSOs need to update managers and S&O survey assignments each survey round
* PM Management document lives [here](https://docs.google.com/spreadsheets/d/1d84x7HHOMgnQM78dYLY9vHqf-jLfYmpH8YGHEDezGNs/edit#gid=249348654)
* Timing: Happens during a predefined window ahead of each survey round, 2-3 weeks before a survey round opens

#### Steps to Update (Beginning Of Year)

* Go to the [PM Management Document](https://docs.google.com/spreadsheets/d/1d84x7HHOMgnQM78dYLY9vHqf-jLfYmpH8YGHEDezGNs/edit#gid=249348654). 
* Update dates for this round.
* Insert any new schools (later: create links to filter views for each school).
        ![](images/survey_annual_1.png)

* In the S&O Assignments tab, unhide Column A, and run SQL query in gabby database.
* Copy results table, and overwrite the first five columns in the S&O Assignments tab.
* Remove any existing data in the S&O Assignments columns (Highlight all - Delete).
        ![](images/survey_annual_2.png)      

* To create filter view for new schools:
    * Data > Filter Views > Create New Filter View
    * Name the filter the new school name
    * Set the range to A2 to End of Row, Last Column
        ![](images/survey_annual_3.png)

    * Copy link for filter view, insert link on the start page of PM Management Document.
        ![](images/survey_annual_4.png)

* In the next few steps, we’ll plug in the information for the three survey management columns:
    * Should take surveys this round
    * TNTP/Insight Survey Assignment
    * Winter Engagement Survey Assignment

* For column ‘Should take surveys this round.’ do the following:
    * Set the following groups to ‘Yes - Should take manager survey only’
        * Primary Site IN (Room 9, Room 10, Room 11)
        * Primary_job IN (Senior Custodian, Security, Custodian)
    * Set everyone else to ‘Yes’.
    * Later: be sure to ask the T&L, KIPP Forward, and Ops teams if they want to have teammates complete S&O surveys. If they do, those teammates will need to have Should take surveys this round to “Yes.”

* For column ‘TNTP/Insight Survey Assignment’ do the following:
    * Create a temporary tab and put the TNTP Insight Survey assignments (that were most recently submitted to KIPP Foundation. It should in Box) into it
    * Index-match the TNTP/insight assignments into the ‘S&O Assignments’ tab
    * Copy the data and paste values back into the tab (so that the formula is overwrite)
    * Delete the temporary tab

* For column ‘Engagement Survey Assignment’ do the following:
    * Unhide the ‘Engagement Survey Assignment’ tab. This tab is a dictionary of titles to ‘Engagement Survey Assignment’ selection.
    * Index-match the engagement survey assignment dictionary from the ‘Engagement Survey Assignment’ tab into the ‘S&O Assignments’ tab

        ![](images/survey_annual_5.png)

    * For any job titles that do not have an engagement survey assignment, update the dictionary with the correct assignment (check if you’re unsure)
    * Copy the data and paste values back into the tab (so that the Index-match formula is overwritten).
    * Re-hide the ‘Engagement Survey Assignment’ tab

#### Steps to Update (Middle Of Year & End of Year)

* Go to PM Management Document.
* Update dates for this round.
* Duplicate ‘S&O Assignments’ tab. Run SQL Query (as in BOY). In the next few steps, you’re going to update the survey roster and keep the survey assignments from last round
* Go back to the original ‘S&O Assignment’ tab
* Copy results table, and overwrite the first five columns in the S&O Assignments tab.
* Delete data in ‘S&O Assignments’ columns and in the columns (referred to below as the three survey management columns)
    * Should take surveys this round
    * TNTP/Insight Survey Assignment
    * Winter Engagement Survey Assignment
* Run INDEX MATCH to ‘S&O Assignments’ (Original) to pre-populate assignments in the three survey management columns and in the S&O assignments columns from last round. 

    Formula: ```=IFERROR(INDEX('Copy of S&O Assignments'!$A$2:$T$3566,MATCH($A3,'Copy of S&O Assignments'!$A:$A,0),MATCH(K$2,'Copy of S&O Assignments'!$2:$2,0)),"")```

* Still in the original ‘S&O Assignments’ tab, highlight the columns with the S&O assignments and the three survey management columns (H-T in the screenshot below). Copy the data, and repaste the values into the cells. You are overwriting the index-match formula with the raw assignments.

    ![](images/survey_annual_6.png)

* Delete the ‘Copy of S&O Assignments’ tab

#### Final Checks Before Sending to DSOs and School Leaders

* Spot check some managers in column "ADP Manager + Whetstone Coach [Do Not Edit]” to ensure that the feed is correct
* Check the ‘Survey Audits’ tab to make sure the columns are lining up and that the counts are working properly
* Go to the ‘Teacher Goals Exemptions’ tab. This tab contains a record of all staff exempted from Teacher Goals in prior and current years. A hidden Column A automatically tags the current year to new entries. Rows with prior year entries are hidden.
    * Update the dates in the headers
    * In the beginning of the year, Update the formula that’s hidden in Column A, so that any new entries are tied to the correct year
    * Hide Column A and any rows records that were submitted for previous school year

    ![](images/survey_annual_7.png)

* Double Check the links on the ‘S&O Start Here’ tab

---

### Insight Survey Tracking


---

### So, what’s actually happening on all of the tabs of the PM Management Document?

---

### Survey Tracker

