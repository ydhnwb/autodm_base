# autodm_base
This is a twitter bot that works like others auto base account (tubirfess, askmenfess etc). Built using python3.

## Please read!
- If you want some insight of this repo look likes, please go to my tutorial https://www.youtube.com/watch?v=_U5Uhf4odss <br>
- I've created some comment in the code.
- Please use python version 3.x

# Example
- Example of how this bot works you can see here https://twitter.com/txtdrtaurus <br>
- or here with some little changes https://twitter.com/imgprocessing <br>
- Screenshot (I use other keyword in this case: 'txt')


<img src="https://pbs.twimg.com/media/EXwH9O7XkAIlxiD?format=jpg&name=large" width="400" height="600">
<img src="https://pbs.twimg.com/media/EXwH-VpVAAI1-54?format=jpg&name=large" width="400" height="800">



# Misc
Of course this bot still not perfect. You can customize by your own
- you can upload a video with low, med, or high quality, check my code, <br>
- you can add gifs support by yourself by adding more elif type == 'gifkey', read twitter api doc please <br>

# How to use this app
## Windows
-> make sure you already have python installed <br>
-> git clone https://github.com/ydhnwb/autodm_base.git <br>
-> change all the API KEY in constants.py with your own <br>
-> open cmd, go to this project's directory <br>
-> activate Scripts\activate <br>

run app.py using syntax: python app.py <br>
(if you have some problem with library, run this: pip install -r requirement.txt)

## Linux
-> make sure you already have python installed <br>
-> git clone https://github.com/ydhnwb/autodm_base.git <br>
-> change all the API KEY in constants.py with your own <br>
-> open terminal, go to this project's directory <br>
-> source env_linux/bin/activate <br>

run app.py using syntax: python3 app.py <br>
(if you have some problem with library, run this: pip install -r requirement.txt)

# Bugs
- I dont know why but the video sometimes uploaded, sometimes it doesnt. Like 60-70% successfully uploaded. Very hard to debug
