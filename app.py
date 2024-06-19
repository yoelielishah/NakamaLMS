from flask import Flask, render_template, jsonify

app = Flask(__name__)

COURSES = [
   {
    'id': 1,
    'course_name': 'Chatbot and AI Intergretion',
    'course_level': 'Beginner',
    'course_duration': '2 months',
    'course_fee': 'Ksh 50,000',
    
   },
  
   {
    'id': 2,
    'course_name': 'CRM and Documentation Management',
    'course_level': 'Beginner',
    'course_duration': '2 months',
     'course_fee': 'Ksh 30,000',

   },

   {
    'id': 3,
    'course_name': 'Fintech Solutions',
    'course_level': 'Beginner',
    'course_duration': '2 months',
     'course_fee': 'Ksh 40,000',

   },

   {
    'id': 4,
    'course_name': 'Customer Service Solutions',
    'course_level': 'Beginner',
    'course_duration': '2 months',
     'course_fee': 'Ksh 20,000',

   },

   {
    'id': 5,
    'course_name': 'Digitalization Services',
    'course_level': 'Beginner',
    'course_duration': '2 months',
     'course_fee': 'Ksh 30,000',

   },

   {
    'id': 6,
    'course_name': 'Contact Service Solutions',
    'course_level': 'Beginner',
    'course_duration': '2 months',
     'course_fee': 'Ksh 20,000',

   },

   {
    'id': 7,
    'course_name': 'E-Learning and Training Programs',
    'course_level': 'Beginner',
    'course_duration': '2 months',
     'course_fee': 'Ksh 20,000',

   },

   {
    'id': 8,
    'course_name': 'Workflow Automation',
    'course_level': 'Beginner',
    'course_duration': '2 months',
     'course_fee': 'Ksh 50,000',

   },

  {
    'id': 9,
    'course_name': 'Customer Relationship Management',
    'course_level': 'Beginner',
    'course_duration': '2 months',
     
  }
]



#html route
@app.route('/')
def hello_world():
  return render_template('home.html',  
                         course = COURSES )

#html route
@app.route('/contactus.html')
def contactus():
  return render_template('contactus.html')

#api route
@app.route('/api/courses')
def online_courses():
  return jsonify(COURSES)  

  

if __name__ == "__main__":
  app.run(debug=True)