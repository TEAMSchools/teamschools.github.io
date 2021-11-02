
# Performance Management 

## Excellent Teaching Rubric

### Background
Evaluation scores are recorded in Whetstone/SchoolMint Grow three times annually. 

### Performance Management Document

* Content TBD

### Lockbox


After a round of performance management scores are finalized and normed, the data is put into a lockbox. Scores are made visible to teachers and no longer editable.


Confirm that schools have completed their ETR scores. In the event that some haven’t (see below), check with the school leaders and confirm whether an extension is needed.

![](images/lockbox_1.png)


Open up the Teacher Goals Dashboard and navigate to the Lockbox_process tab (note: this tab is only accessible on Tableau Desktop)

![](images/lockbox_2.png)
![](images/lockbox_3.png)


Refresh all extracts and set the filters to the correct year and term

![](images/lockbox_4.png)


Open the worksheet tab and activate the data by clicking anywhere on the sheet

![](images/lockbox_5.png)

IF SOME SCHOOLS NEED AN EXTENSION (otherwise skip this step): Add Primary Site to rows

![](images/lockbox_6.png)

Open the Worksheet Drop-down, go to Copy-> Data

![](images/lockbox_7.png)

Open an Excel workbook and paste values into the Excel sheet

IF SOME SCHOOLS NEED AN EXTENSION (otherwise skip this step): Filter the schools that aren’t ready to upload or if you’re loading at the end of an extension filter the schools that have not been loaded yet. Filter and delete the rows completely.

![](images/lockbox_8.png)

![](images/lockbox_9.png)

Delete the Primary Site Column

![](images/lockbox_10.png)

Confirm that the data looks right.

![](images/lockbox_11.png)

Save the Excel table as a csv. The format should be "pm.teacher_goals_lockbox-yyyy q#". For an extension submission the format should be “pm.teacher_goals_lockbox-<schools>-yyyy q#”.

![](images/lockbox_12.png)

Upload to the csv to [Google Cloud Storage](https://www.google.com/url?q=https://console.cloud.google.com/home/dashboard?project%3Dfivetran-167215%26pli%3D1&sa=D&source=editors&ust=1635860896326000&usg=AOvVaw2_54CQk74uZMV3nK-8hFpz) (Storage-> Browser-> Buckets-> data-robot-gcs-> pm-> teacher_goals_lockbox )

![](images/lockbox_13.png)
![](images/lockbox_14.png)

Save the csv on Google Drive. (Data Team -> Data Repository -> Teacher Goals Lockbox)

![](images/lockbox_15.png)

When FiveTran refreshes (every ~15 minutes), the locked scores will show up in the dashboard. Check it by running ```SELECT * FROM pm.teacher_goals_lockbox``` in SQL.

![](images/lockbox_16.png)
    
Confirm that stored values are displaying on tableau.pm_teacher_goals by running ```SELECT * FROM tableau.pm_teacher_goals```

![](images/lockbox_17.png)

If all of the schools are done, you can turn the refresh for the Teacher Goals dashboard back on and Publish.

![](images/lockbox_18.png)