# AmongUsCompetitive vs. AmongUsMemes


### Problem Statement 
Through Natural Language Processing, people can give computers to understand text and spoken words. This project is aimed to using Push’s API and getting data from two subreddits, AmongUsCompetitive and AmongUsMemes, to effectively predict which subreddit the title came from and predicting new titles.  



### Data Dictionary 



###### Data Dictionary for the Models

|Feature|Type|Dataset|Description|
|---|---|---|---|
|Subreddit|*object*|amongus_comp_memes.csv | The subreddit the title came from 
|Title|*object*|amongus_comp_memes.csv | The title of the post


### Brief Summary and Interesting Findings

In this analysis, I set out to see if a model can predict which subreddit a title came from. Before building the models, I used Push's API to get 1,093 rows of data for the modeling process. After this, I did EDA to figure out what each subreddit had. What was interesting is that reddit allows people to submit posts with vulgar words and I deleted those rows because it was offensive. What was also interesting was that the memes subreddit had a lot of titles with 'sus' and 'sussy' which I believe helped the models predict those types of titles better. I set out to also see the first and last word in each title, and the last two characters in the titles. Something that was eye-catching was that I expected the memes subreddit to have a lot of emojis as the last word, there was only one emoji that appeared in the top 15. Also, as for the last two characters, I expected the memes one to have ':)' or ':(' but none of these actually came up, besides an emoji. For the models, I used decision tree and random forest algorithms to build models and make predictions. The random forest models did better in general so I expanded on these models in predicting random words or phrases and seeing how it would perform. It was performing well on predicting words or phrases that fit under the memes subreddit, but not the best job in predicting for the competitive subreddit, such as 'need a team'. This may be due to the very random subreddit titles and posts that are on these pages, or my model is predicting the memes one because it contained a variety of different titles and they were very general. 


### Conclusions/Recommendations

In this project, making a model using natural language processing was more difficult. For the random forest models, both models had difficulty predicting a phrase like ‘need a team’. It would predict AmongUsMemes when expecting AmongUsCompetitive. It seems as though there are random titles in both subreddits that can make predicting certain phrases difficult. In all, the random forest did better job at predicting. I recommend in the future at looking more into what each subreddit contains more closely for the model to predict better. 