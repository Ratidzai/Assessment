
#My Instructions on how I did this assessment3

#QUESTION 1
*I used VS code to do the assessment
*I used global variable so that it can print the output which is 4

#QUESTION 2
*I installed pytest and ran a command to check if it was installed
*I used $sudo pip install -U to install it
*I change the value which was 3 to 4 in order to pass the test
*I tested by added 5 as well and the test failed
*I used the $ pytest question2.py to run the function

#QUESTION 3
*I imported os and requests firstly
*I wrote the script as instructed to loop and hit a website
* I then proceeded to use the following command $ export times is 5
* To check the env value I used $ echo $ times
*The command I used to run the script is $python3 question3.py 

QUESTION 4
*I installed docker
* Next thing I did was install curl with this command
-sudo apt install curl

*I used question 3 as the python script with this command to run it
- $python3 question3.py(I used python3 because of having python 3.10.4)

#Creating the docker image
*I used the dockerfile as the starting point 
*secondly I used the command 
docker build . -t python-image(name of my image)
*All the dependencies were installed successfully from step 1 to 7
step 1 - From python
step 2 -Run pip3 install requests
step 3 - WORKDIR "/app"
step 4 - COPY question3.py
Step 5 - ENV site=http://api.open-notify.org/astros.json
Step 6 - ENV times=5
 Step 7 - CMD ["python3", "question3.py"]

 * I used the command $ docker images to check if the new images has been installed
 THE NAME OF MY IMAGE IS python-image

 *FINALLY
 - $ docker run -e times=5 python-image is the command I used to run the DOCKER.





