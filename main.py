import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_data.csv")
# print(df.head())

# print(df.info())

#Data clean
df=df.dropna()
# print(df.info())

#Title-Bar Graph 
# title_values=df['type'].value_counts()

# plt.bar(title_values.index,title_values.values,color=['skyblue','orange'])

# plt.xlabel("Type")
# plt.ylabel("Count")
# plt.title("No of Movies and Tv Shows on Netflix")
# plt.tight_layout()
# plt.savefig("Movies_vs_TvShows.png",dpi=300,bbox_inches='tight')
# plt.show()

# #genre-Pie Chart
# genre_values=df['genre'].value_counts().head(10)
# plt.pie(genre_values.values,labels=genre_values.index,autopct='%1.1f%%')
# plt.title("Percentage of Genre on Netflix")
# plt.tight_layout()
# plt.savefig("Genre Percentage.pdf")
# plt.show()

# #release_year-Histogram
# plt.figure(figsize=(10, 8)) 
# plt.hist(df['release_year'],bins='auto',color='purple',edgecolor='black')
# plt.xlabel("Year")
# plt.ylabel("Movies/TvShows released")
# plt.title("Movies/TvShows released per Year")
# plt.tight_layout()
# plt.savefig("Movies_Tvshows_Histogram.png",dpi=300,bbox_inches='tight')
# plt.show()

# #Country Movies Release - Pie chart
# country_values=df['country'].value_counts().head(10)
# plt.figure(figsize=(8,6)) 
# plt.barh(country_values.index,country_values.values)
# plt.xlabel("No of movies/Tvshows released")
# plt.ylabel("Country")
# plt.title("Top 10 countries Movies/TvShows released")
# plt.tight_layout()
# plt.savefig("Country_release_pie_chart")
# plt.show()

#Subplot
# content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)

# fig,ax=plt.subplots(1,2,figsize=(12,5))

# ax[0].plot(content_by_year.index,content_by_year["Movie"],color='skyblue')
# ax[0].set_title("Movies released per year")
# ax[0].set_xlabel("Year")
# ax[0].set_ylabel("No of Movies")

# ax[1].plot(content_by_year.index,content_by_year["TV Show"],color='red')
# ax[1].set_title("TV Show released per year")
# ax[1].set_xlabel("Year")
# ax[1].set_ylabel("No of TV Show")

# fig.suptitle("Comparision of TV Show and Movie released per year")
# plt.tight_layout()
# # plt.savefig("Tv_Show_Movies_per_year",dpi=300,bbox_inches="tight")

# plt.show()




