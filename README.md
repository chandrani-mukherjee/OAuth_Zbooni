Introduction:
     Django OAuth Toolkit is used in this project to used tokenization. Browser and API postman support provided to access the endpoints.  The detailed steps to be followed are described below in sequence. Except the first registration all are bearer token based authentication.
     Key Features:
•	Virtual Env used
•	Custom User Model
•	Django OAuth Toolkit
•	API View
•	Bearer token
•	Activating user on receipt of token using login
•	Well documented code
•	User documentation provided for API 
•	

Steps to be followed
1.	To obtain a valid access_token first we must register an application. DOT has a set of customizable views you can use to CRUD application instances, just point your browser at:

http://localhost:8000/o/applications/

 ![image](https://github.com/user-attachments/assets/0b847d0c-1d68-4406-892f-813d5a87bc99)

2.	Registration: At this point we’re ready to request an access_token.
 ![image](https://github.com/user-attachments/assets/039eb56e-7cfc-4915-93da-9b56cd6917da)

3.	User Activation:  Provide email ID and token shared to activate user
 ![image](https://github.com/user-attachments/assets/b975bce1-820d-4db4-a372-cd2c934e6da5)
 ![image](https://github.com/user-attachments/assets/2ea644c1-a70c-47f8-8d2c-a3596272d8e3)
  
4.	Login: the endpoint should require email and password, and if correct, responds with an OAuth2 bearer token.                                                                                                                                                                                                                             
![image](https://github.com/user-attachments/assets/a4fa3d4a-d29c-4907-8f92-0d806962acf6)


5.	Change Password

 ![image](https://github.com/user-attachments/assets/a423b328-bf87-487c-ba7c-9464cefe6700)
 ![image](https://github.com/user-attachments/assets/790b64bd-2988-4c20-86d9-5bf3033da36e)

6.	Users list:

![image](https://github.com/user-attachments/assets/e61be5f1-6229-4683-a443-354f4eaaf7ad)
 

7.	Postman Collection : Collection attached
 
![image](https://github.com/user-attachments/assets/6adec656-1ebe-43a8-bf88-a4a2ef03d6f9)
