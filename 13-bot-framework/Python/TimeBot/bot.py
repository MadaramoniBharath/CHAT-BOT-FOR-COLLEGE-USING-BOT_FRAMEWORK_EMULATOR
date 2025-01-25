from botbuilder.core import ActivityHandler, MessageFactory
from botbuilder.schema import Activity

class MyBot(ActivityHandler):
    async def on_message_activity(self, turn_context):
        user_message = turn_context.activity.text.strip().lower()

        # Define responses for common college queries
        college_responses = {
            "what courses do you offer?": "We offer a variety of courses including Computer Science,Electronics and Communication Engineering and CIVIL engineering vist websit https://tkrec.ac.in/#",
            "how do i apply?": "You can apply online through our website. Make sure to check the application deadlines https://tkrec.ac.in/admissions-ug/",
            "what is the campus like?": "Our campus features modern facilities, libraries, and recreational areas. It's a vibrant place to study!",
            "do you have scholarships?": "Yes, we offer various scholarships based on merit and need. Please check our financial aid page for more details https://tkrec.ac.in/",
            "what are the admission requirements?": "Admission requirements vary by program. Generally, you need a high school diploma and standardized test scores.",
            "what is the tuition fee?": "Tuition fees vary by program. Please visit the tuition page on our website for detailed information. ",
            "when does the semester start?": "The semester typically starts in September, but please check our academic calendar for specific dates. https://tkrec.ac.in/",
            "what extracurricular activities do you offer?": "We offer a wide range of extracurricular activities, including clubs, sports, and volunteer opportunities.",
            "when the semister results will be announced?": "semister results will be accounced after 45 days of written",
            "where we have to check the semister results?": "you can check your results by below link is https://tkrecautonomous.org/BETEPortal/Login.aspx",
            "do we have ncc or nss in the college?" : "Yes we have NCC and NSS for the students",
            "is college provide placements?": "Yes we will provide college placements in in the mid third year and final years https://tkrec.ac.in/placement-news/",
            "what is the highest package in college placements?":"the highest package in college placements is 21LPA in Meesho Company https://tkrec.ac.in/placement-news/",
            "can i know the list of students placed in the college placements?": " yes you can check the list by clicking on below link https://tkrec.ac.in/placement-details/ ",
            "does your college conduct any cultural activities?": "Yes we conduct different cultural activities https://www.youtube.com/watch?v=QfKCCM4cil8",
            "can you provide the contact details of csg department": "yes click on below link you will get all details https://tkrec.ac.in/computer-science-and-design/",
            "can you provide the contact details of cse department" : "yes click on below link you will get all details https://tkrec.ac.in/department-cse/",
            "can you provide the contact details of ece department ": "yes click on below link you will get all details https://tkrec.ac.in/department-ece/",
            "can you provide the contact details of aiml department" : "yes click on below link you will get all details https://tkrec.ac.in/artificial-intelligence-machine-learning/",
            "can you provide the contact details of eee department" : "yes click on below link you will get all details https://tkrec.ac.in/department-eee/",
            "can you provide the contact details of it department" : "yes click on below link you will get all details https://tkrec.ac.in/department-it/",
            "can you provide the contact details of humanity and sciences department" : "yes click on below link you will get all details https://tkrec.ac.in/department-hs/",
            "can college have gym": "Yes we have Gym in the college",



            
        }

        # Get a response based on user message
        response_message = college_responses.get(user_message, "I'm sorry, I didn't understand that. Can you please ask something else about the college?")
        
        # Send the response back to the user
        await turn_context.send_activity(MessageFactory.text(response_message))