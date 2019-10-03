## 2. Frequency Distribution ##

fandango_distribution = norm_reviews.Fandango_Ratingvalue.value_counts().sort_index()
imdb_distribution = norm_reviews.IMDB_norm.value_counts().sort_index()
print(fandango_distribution)
print(imdb_distribution)

## 4. Histogram In Matplotlib ##

fig, ax = plt.subplots()
ax.hist(norm_reviews.Fandango_Ratingvalue, range=(0,5))
plt.show()

## 5. Comparing histograms ##

fig = plt.figure(figsize=(5,20))
axes = [fig.add_subplot(4,1,x) for x in range(1,5)]
col_names = ["Fandango_Ratingvalue", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm"]
plt_titles = ["Distribution of {} Ratings".format(x) for x in ["Fandango", "Rotten Tomatoes", "Metacritic", "IMDB"]]
for axis, col_name, plt_title in zip(axes, col_names, plt_titles):
    axis.hist(norm_reviews[col_name], 20, range=(0,5))
    axis.set_ylim((0,50))
    axis.set_title(plt_title)
    
plt.show()

## 7. Box Plot ##

fig, ax = plt.subplots()
ax.boxplot(norm_reviews.RT_user_norm)
ax.set_ylim(0,5)
ax.set_xticklabels(['Rotten Tomatoes'])
plt.show()

## 8. Multiple Box Plots ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']

fig, ax = plt.subplots()
ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_ylim(0,5)
plt.show()