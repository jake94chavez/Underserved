# Underserved

<b> Mission Statement </b><br/>
Independent developers do not have the resources to do their own market research. We are creating a tool that provides these developers with a platform, to expedite their own market research, based on convenient access to aggregated Steam game data.<br/>
"We’ve got game/tag/metascore data, and we’re giving folks a few options to select tags with the goal of finding underserved niches in the game market."

<b>Target User</b><br/>
The independent game developer, who is looking to gain a strategic edge, by using information that is already available.<br/>

"The United States video game industry employs an estimated 65,678 direct employees as of 2016. 99.7% of American-based
companies across all subgroups employ less than 500 employees with 91.4% of all American-based game companies
employing less than 30 employees. This means that almost 100% of American game companies are considered small businesses
under the qualifications set by the Small Business Administration. Only a handful of AAA game publishers employ more than 500
employees and are considered major corporations."<br/>
http://www.theesa.com/wp-content/uploads/2017/02/ESA-VG-Industry-Report-2016-FINAL-Report.pdf
<br/><br/>
<b>Technologies</b><br/>
Python<br/>
Django<br/>
HTML/CSS/JS<br/>
PostGres<br/>
Bootstrap<br/>

<b>Getting Started</b></br>
Download this repo<br/>
Install requirements: `$ pip3 install -r requirements.txt`<br/>
Start server        : `$ python3 manage.py runserver`<br/>

<b>Trello</b><br/>
https://trello.com/b/kMQuZJhT/underserved<br/>
  
<b>Display</b><br/>
The color palette:<br/>
Dark Grey : #5A5656<br/>
Light Grey: #B6AEAE<br/>
Blue-Grey : #5488DC<br/>

<b>Routes</b><br/>

HTTP Method|Endpoint
---|---
|GET|/index|
|POST|/index|
|GET|/results|
|GET|/profile|
|PUT|/profile|
|DELETE|/profile|

<br/>
<b>WIREFRAMES</b><br/>
![Index Page](https://github.com/jake94chavez/Underserved/blob/chanten_branch/index.png)<br/><br/>
search results page<br/>
![Search Results](Underserved/searchResults.png)<br/><br/>
user profile page<br/>
![User Profile](https://github.com/jake94chavez/Underserved/blob/master/userProfile.png)<br/><br/>
