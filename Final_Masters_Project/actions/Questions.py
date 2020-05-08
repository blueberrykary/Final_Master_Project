# ## Karen Salinas
# ## CSC 590
# Questions that student may ask
api_key = "AIzaSyAeAYpLBY6vo8ZSECeMadGx5Y9oLHcUw6s"
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import json
import re
import sqlalchemy
import webbrowser
import pandas as pd
import googlemaps
from dbConnect import getData

##==============================================================================#
##==============================================================================#
##==============================================================================#
class Action_FAFSA_info(Action):

    def name(self) -> Text:
        return "action_FAFSA"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        fafsa_application = tracker.get_slot("FAFSA_APP")

        q = 'select f.fafsa_type from school as s INNER JOIN offers_fafsa as oof ON s.school_id = oof.school_id INNER JOIN fafsa as f ON oof.fafsa_id = f.fafsa_id'
        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)

        #Print out the fafsa types
        details = "Types of Fafsa offered at CSUDH"
        set_one = str(data[0][0]) + "                              " +  str(data[1][0]) + "                              " + str(data[2][0])
        #combine the message
        link = '<a href="https://www.csudh.edu/financial-aid/types-aid/">FAFSA types</a>'
        set_combined = details + "\n" +  set_one + "\n" + link
        # output message
        fafsa_appp = set_combined
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(fafsa_appp))
        #returning the slot for fafsa
        return [SlotSet("fafsa_appp", fafsa_application)]

##==============================================================================#
##==============================================================================#
##==============================================================================#
class Action_Enrollment(Action):

    def name(self) -> Text:
        return "action_Eenrollment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        unii_enrollment = tracker.get_slot("uni_enroll")
        q = 'select e.semester from school as sc FULL OUTER JOIN attends as a ON a.school_id = sc.school_id FULL OUTER JOIN user_type as ut ON a.id = ut.id FULL OUTER JOIN views_enrollment as ve ON ut.id = ve.id FULL OUTER JOIN enrollment as e ON ve.enrollment_id = e.enrollment_id WHERE ut.id = 1 AND e.enrollment_id = 5 OR ut.id = 2 AND e.enrollment_id = 6 '
        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)

        # list out the semester
        message = "Semesters available to view:"

        opt = "==========================="
        set_one = str(data[0][0]) + "<br/><br/>" + str(data[1][0])
        opt2 = "==========================="

        set_combined  = message + "\n" + opt + "\n" + set_one + "\n" + opt2

        university_enroll = set_combined
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(university_enroll))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("university_enroll", unii_enrollment)]
##==============================================================================#
##==============================================================================#
##==============================================================================#
##========================CAMPUS ============================================##
class Action_Campus(Action):

    def name(self) -> Text:
        return "action_campus_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        campus_info = tracker.get_slot("campus_CSUDH")

        campus_information = ""
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="".format(campus_information))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("campus_information", campus_info)]

class Action_Campus_Tour(Action):

    def name(self) -> Text:
        return "action_oncampus_tour"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        campus_tour_info = tracker.get_slot("campus_tour_CSUDH")
        q = 'select ct.campus_desc from school as s FULL OUTER JOIN shows_campus as sc ON sc.school_id = s.school_id FULL OUTER JOIN campus as c ON sc.campus_id = c.campus_id FULL OUTER JOIN provides_tours as pt ON pt.campus_id = c.campus_id FULL OUTER JOIN campus_tours as ct ON ct.campus_tour_id = pt.campus_tour_id'
        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)
        message = "Prospective Student Tours"

        details = str(data[0][0])


        set_one = str(data[1][0])  + " <br/><br/> " +  str(data[2][0])  + " <br/><br/> " +  str(data[3][0])  + " <br/><br/> " +  str(data[4][0])
        set_combined = message + "<br/><br/>" + details + "<br/><br/>" +  set_one + "\n\n"


        message2 = "Group Tours" + "<br/><br/>"

        set_two = str(data[5][0]) + "<br/><br/>" + str(data[6][0])

        link = '<a href = "https://www.csudh.edu/future-students/more-info/visit-csudh/schedule-a-tour/">More Tour Information</a>'

        set_combined2 = message2 + set_two

        combined = set_combined + set_combined2 + "\n\n" + link
        on_campus_tour_info = combined
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(on_campus_tour_info))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("on_campus_tour_info", campus_tour_info)]

class Action_Campus_Map(Action):

    def name(self) -> Text:
        return "action_campusmap"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        campus_mapCSUDH = tracker.get_slot("campus_map_CSUDH")
        # api_key = "AIzaSyAeAYpLBY6vo8ZSECeMadGx5Y9oLHcUw6s"
        # url =  "https://maps.googleapis.com/maps/api/staticmap?"
        # location = input("Enter location: ")
        # center = location
        # zoom = 15
        # r = requests.get(url + "center" + center + "&zoom= " + str(zoom) + "&size =400x400&key=" +  api_key)
        # print(url + "center=" + center + "&zoom=" + str(zoom) + "&size=400x400&key=" + api_key)
        # f = open('/home/blueberrykary/Desktop/b.png', 'wb')
        # f.write(r.content)
        # f.close()

        #map that was received from google static maps
        ##Geocoding map coordinates
        # df = pd.DataFrame({
        #     'address':['CSUDH']
        #     })
        #
        # gmaps_key = googlemaps.Client(key = "AIzaSyAeAYpLBY6vo8ZSECeMadGx5Y9oLHcUw6s")
        #
        # df['Lat'] = None
        # df['Lon'] = None
        #
        # for i in range(len(df)):
        #     geocode_result = gmaps_key.geocode(df.loc[i, 'address'])
        #     try:
        #         lat = geocode_result[0]["geometry"]["location"]["lat"]
        #         lng = geocode_result[0]["geometry"]["location"]["lng"]
        #         df.loc[i, 'Lat'] = lat
        #         df.loc[i, 'Lon'] = lng
        #     except:
        #         lat = None
        #         lng = None


        link = '<iframe width="180" height="180" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/place?key=AIzaSyAeAYpLBY6vo8ZSECeMadGx5Y9oLHcUw6s&q=California+State+University+Dominguez+Hills,Carson+CA" allowfullscreen></iframe>'

        campusMapCSUDH = link
        #uttering message containing the response from slot
        dispatcher.utter_message(text="{}".format(campusMapCSUDH))

        #returning the slot for meant for incoming graduate students
        return [SlotSet("campusMapCSUDH", campus_mapCSUDH)]


class Action_Campus_Employment(Action):

    def name(self) -> Text:
        return "action_employment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        campus_employment = tracker.get_slot("campus_employment_CSUDH")
        q = 'select campus_e.employ_description from school as s FULL OUTER JOIN shows_campus as sc ON sc.school_id = s.school_id FULL OUTER JOIN campus as c ON sc.campus_id = c.campus_id FULL OUTER JOIN contains_employment as ce ON c.campus_id = ce.campus_id FULL OUTER JOIN campus_employment as campus_e ON ce.campus_employ_id = campus_e.campus_employ_id ORDER BY campus_e.campus_employ_id LIMIT 5'
        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)
        details = str(data[0][0])
        seperator = "================================================"
        set_one = str(data[1][0])  + " <br/> " +  str(data[2][0])  + " <br/> " +  str(data[3][0])  + " <br/> " +  str(data[4][0])
        set_combined = details + "\n" + seperator + "\n" +  set_one + "\n\n"
        #-----------------------------------------------------------------------#
        #query2
        q2 = 'select campus_e.employ_description from school as s FULL OUTER JOIN shows_campus as sc ON sc.school_id = s.school_id FULL OUTER JOIN campus as c ON sc.campus_id = c.campus_id FULL OUTER JOIN contains_employment as ce ON c.campus_id = ce.campus_id FULL OUTER JOIN campus_employment as campus_e ON ce.campus_employ_id = campus_e.campus_employ_id ORDER BY campus_e.campus_employ_id LIMIT 5 OFFSET 5'
        #pass the sql query to the getData method and store the results in `data` variable.
        data2 = getData(q2)
        details2 = str(data2[0][0])
        seperator2 = "================================================"
        set_one2 = str(data2[1][0])  + " <br/> " +  str(data2[2][0])  + " <br/> " +  str(data2[3][0])  + " <br/> " +  str(data2[4][0])
        set_combined2 = details2 + "\n" + seperator2 + "\n" +  set_one2 + "\n\n"
        #-----------------------------------------------------------------------#
        # query3
        q3 = 'select campus_e.employ_description from school as s FULL OUTER JOIN shows_campus as sc ON sc.school_id = s.school_id FULL OUTER JOIN campus as c ON sc.campus_id = c.campus_id FULL OUTER JOIN contains_employment as ce ON c.campus_id = ce.campus_id FULL OUTER JOIN campus_employment as campus_e ON ce.campus_employ_id = campus_e.campus_employ_id ORDER BY campus_e.campus_employ_id LIMIT 1 OFFSET 10'
        #pass the sql query to the getData method and store the results in `data` variable.
        data3 = getData(q3)
        details3 = str(data3[0][0])
        set_combined3 = details3 + "\n\n"
        #-----------------------------------------------------------------------#
        # query4
        q4 = 'select campus_e.employ_description from school as s FULL OUTER JOIN shows_campus as sc ON sc.school_id = s.school_id FULL OUTER JOIN campus as c ON sc.campus_id = c.campus_id FULL OUTER JOIN contains_employment as ce ON c.campus_id = ce.campus_id FULL OUTER JOIN campus_employment as campus_e ON ce.campus_employ_id = campus_e.campus_employ_id ORDER BY campus_e.campus_employ_id LIMIT 5 OFFSET 11'
        #pass the sql query to the getData method and store the results in `data` variable.
        data4 = getData(q4)
        #Print out the course details for 595
        details4 = str(data4[0][0])
        seperator4 = "================================================"
        set_one4 = str(data4[1][0])  + " <br/> " +  str(data4[2][0])  + " <br/> " +  str(data4[3][0])  + " <br/> " +  str(data4[4][0])
        set_combined4 = details4 + "\n" + seperator4 + "\n" +  set_one4 + "\n\n"
        #-----------------------------------------------------------------------#
        #query5
        q5 = 'select campus_e.employ_description from school as s FULL OUTER JOIN shows_campus as sc ON sc.school_id = s.school_id FULL OUTER JOIN campus as c ON sc.campus_id = c.campus_id FULL OUTER JOIN contains_employment as ce ON c.campus_id = ce.campus_id FULL OUTER JOIN campus_employment as campus_e ON ce.campus_employ_id = campus_e.campus_employ_id ORDER BY campus_e.campus_employ_id LIMIT 6 OFFSET 16'
        #pass the sql query to the getData method and store the results in `data` variable.
        data5 = getData(q5)
        details5 = str(data5[0][0])
        seperator5 = "================================================"
        set_one5 = str(data5[1][0])  + " <br/> " +  str(data5[2][0])  + " <br/> " +  str(data5[3][0])  + " <br/> " +  str(data5[4][0]) + " <br/> " +  str(data5[5][0])
        set_combined5 = details5 + "\n" + seperator5 + "\n" +  set_one5 + "\n\n"
        #-----------------------------------------------------------------------#
        message4 = '<a href="https://www.lsucsudh.org/student-employment/">Employment Opportunities</a>'
        output = set_combined + "\n\n" + message4
        campus_employment_stu = output

        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(campus_employment_stu))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("campus_employment_stu", campus_employment)]

##==============================================================================#
##==============================================================================#
##==============================================================================#
class Action_view_course(Action):

    def name(self) -> Text:
        return "action_view_cs_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        course_start = tracker.get_slot("getting_course")

        course_end = ""
        #uttering message containing the school response from slot
        dispatcher.utter_message(text="".format(course_end))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("course_end", course_start)]


##==============================================================================#
##==============================================================================#
##==============================================================================#
class Action_view_spring2020_course(Action):

    def name(self) -> Text:
        return "action_view_spring2020"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        spring_c1 = tracker.get_slot("spring_2020_course1")

        #select the semester, the subject type, the course number, class number, and class time for CSC 590
        q = 'select  e.semester, s.subject_type, c.course_number, cl.class_number, t.day_time, t.start_time, t.end_time, p.fname, p.lname, p.email from school as sc FULL OUTER JOIN attends as a ON a.school_id = sc.school_id FULL OUTER JOIN user_type as ut ON a.id = ut.id FULL OUTER JOIN views_enrollment as ve ON ut.id = ve.id FULL OUTER JOIN enrollment as e ON ve.enrollment_id = e.enrollment_id FULL OUTER JOIN has_course as hc ON e.enrollment_id = hc.enrollment_id FULL OUTER JOIN course as c ON hc.course_id = c.course_id FULL OUTER JOIN contains_subject as csub ON c.course_id = csub.course_id FULL OUTER JOIN subject as s ON csub.subject_id = s.subject_id FULL OUTER JOIN offers_class as oc ON s.subject_id = oc.subject_id FULL OUTER JOIN class as cl ON oc.class_id = cl.class_id FULL OUTER JOIN meets as m ON cl.class_id = m.class_id FULL OUTER JOIN class_time as t ON m.class_time_id = t.class_time_id FULL OUTER JOIN teaches as tt ON cl.class_id = tt.class_id FULL OUTER JOIN professor as p ON tt.professor_id = p.professor_id WHERE ut.id = 1 AND e.enrollment_id = 5 AND t.class_time_id = 16 AND c.course_id = 21'
        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)


        #Print out the course details for 595
        opt = "=============================="
        details = "Course Details"
        set_one = str(data[0][0])
        set_two = str(data[0][1])
        set_three = str(data[0][2])
        set_four = "    Class Number = " + str(data[0][3])
        set_five = "On " + str(data[0][4]) + " at " + str(data[0][5]) + " to " + str(data[0][6])
        set_six = "    Professor: " + str(data[0][7]) + " " + str(data[0][8]) + "\n" + "   Email: " + str(data[0][9])
        opt2 = "=============================="

        set_combined  = opt + "<br/><br/>" + details + "<br/><br/>"+ set_one + "<br/><br/>" + set_two + "<br/><br/>" + set_three
        set_combined2 = " " + set_four + "<br/><br/>" + set_five + "<br/><br/>" + set_six + "<br/><br/>" + opt2

        set_com = set_combined + set_combined2

        spring_2020c1 = set_com

        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(spring_2020c1))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("spring_2020c1", spring_c1)]

##==============================================================================#
##==============================================================================#
##==============================================================================#
class Action_view_spring2020_course2(Action):

    def name(self) -> Text:
        return "action_view_spring20202"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        spring_c2 = tracker.get_slot("spring_2020_course2")

        #select the semester, the subject type, the course number, class number, and class time for CSC 590
        q = 'select  e.semester, s.subject_type, c.course_number, cl.class_number, t.day_time, t.start_time, t.end_time, p.fname, p.lname, p.email from school as sc FULL OUTER JOIN attends as a ON a.school_id = sc.school_id FULL OUTER JOIN user_type as ut ON a.id = ut.id FULL OUTER JOIN views_enrollment as ve ON ut.id = ve.id FULL OUTER JOIN enrollment as e ON ve.enrollment_id = e.enrollment_id FULL OUTER JOIN has_course as hc ON e.enrollment_id = hc.enrollment_id FULL OUTER JOIN course as c ON hc.course_id = c.course_id FULL OUTER JOIN contains_subject as csub ON c.course_id = csub.course_id FULL OUTER JOIN subject as s ON csub.subject_id = s.subject_id FULL OUTER JOIN offers_class as oc ON s.subject_id = oc.subject_id FULL OUTER JOIN class as cl ON oc.class_id = cl.class_id FULL OUTER JOIN meets as m ON cl.class_id = m.class_id FULL OUTER JOIN class_time as t ON m.class_time_id = t.class_time_id FULL OUTER JOIN teaches as tt ON cl.class_id = tt.class_id FULL OUTER JOIN professor as p ON tt.professor_id = p.professor_id WHERE ut.id = 1 AND e.enrollment_id = 5 AND t.class_time_id = 11 AND c.course_id = 20 AND p.professor_id = 12'
        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)


        #Print out the course details for 595
        opt = "=============================="
        details = "     Course Details       "
        set_one = "      " + str(data[0][0]) + "      "
        set_two = "      " + str(data[0][1]) + "      "
        set_three = "      " + str(data[0][2]) + "      "
        set_four = "      " + "Class Number = " + str(data[0][3]) + "      "
        set_five = "      " + "On " + str(data[0][4]) + " at " + str(data[0][5]) + " to " + str(data[0][6]) + "      "
        set_six = "      " + "    Professor: " + str(data[0][7]) + " " + str(data[0][8]) + "\n" + "   Email: " + str(data[0][9]) + "      "
        opt2 = "=============================="

        set_combined  = opt + "<br/><br/>" + details + "<br/><br/>" +  set_one + "\n" + "<br/><br/>" + set_two + "<br/><br/>" + set_three
        set_combined2 = " " + set_four + "<br/><br/>" + set_five + "<br/><br/>" + set_six + "<br/><br/>" + opt2

        set_com = set_combined + set_combined2

        spring_2020c2 = set_com

        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(spring_2020c2))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("spring_2020c2", spring_c2)]

##==============================================================================#
##==============================================================================#
##==============================================================================#
class Action_view_spring2020_course3(Action):

    def name(self) -> Text:
        return "action_view_spring20203"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        spring_c3 = tracker.get_slot("spring_2020_course3")

        #select the semester, the subject type, the course number, class number, and class time for CSC 590
        q = 'select  e.semester, s.subject_type, c.course_number, cl.class_number, t.day_time, t.start_time, t.end_time, p.fname, p.lname, p.email from school as sc FULL OUTER JOIN attends as a ON a.school_id = sc.school_id FULL OUTER JOIN user_type as ut ON a.id = ut.id FULL OUTER JOIN views_enrollment as ve ON ut.id = ve.id FULL OUTER JOIN enrollment as e ON ve.enrollment_id = e.enrollment_id FULL OUTER JOIN has_course as hc ON e.enrollment_id = hc.enrollment_id FULL OUTER JOIN course as c ON hc.course_id = c.course_id FULL OUTER JOIN contains_subject as csub ON c.course_id = csub.course_id FULL OUTER JOIN subject as s ON csub.subject_id = s.subject_id FULL OUTER JOIN offers_class as oc ON s.subject_id = oc.subject_id FULL OUTER JOIN class as cl ON oc.class_id = cl.class_id FULL OUTER JOIN meets as m ON cl.class_id = m.class_id FULL OUTER JOIN class_time as t ON m.class_time_id = t.class_time_id FULL OUTER JOIN teaches as tt ON cl.class_id = tt.class_id FULL OUTER JOIN professor as p ON tt.professor_id = p.professor_id WHERE ut.id = 1 AND e.enrollment_id = 5 AND c.course_id = 18 AND p.professor_id = 16'
        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)


        #Print out the course details for 595
        opt = "=============================="
        details = "Course Details"
        set_one = str(data[0][0])
        set_two = str(data[0][1])
        set_three = str(data[0][2])
        set_four = "    Class Number = " + str(data[0][3])
        set_five = "On " + str(data[0][4]) + " at " + str(data[0][5]) + " to " + str(data[0][6])
        set_six = "Professor: " + str(data[0][7]) + " " + str(data[0][8]) + "\n" + " Email: " + str(data[0][9])
        opt2 = "=============================="

        set_combined  = opt + "<br/><br/>" + details + "<br/><br/>" + set_one + "<br/><br/>" + set_two + "<br/><br/>" + set_three
        set_combined2 = " " + set_four + "<br/>" + set_five + "<br/>" + set_six + "<br/><br/>" + opt2

        set_com = set_combined + set_combined2

        spring_2020c3 = set_com

        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(spring_2020c3))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("spring_2020c3", spring_c3)]

##==============================================================================#
##==============================================================================#
##==============================================================================#
class Action_view_summer2020_course1(Action):

    def name(self) -> Text:
        return "action_view_summer2020"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        summer_c1 = tracker.get_slot("summer_2020_course1")

        q = 'select  e.semester, s.subject_type, c.course_number, cl.class_number, t.day_time, t.start_time, t.end_time, p.fname, p.lname, p.email from school as sc FULL OUTER JOIN attends as a ON a.school_id = sc.school_id FULL OUTER JOIN user_type as ut ON a.id = ut.id FULL OUTER JOIN views_enrollment as ve ON ut.id = ve.id FULL OUTER JOIN enrollment as e ON ve.enrollment_id = e.enrollment_id FULL OUTER JOIN has_course as hc ON e.enrollment_id = hc.enrollment_id FULL OUTER JOIN course as c ON hc.course_id = c.course_id FULL OUTER JOIN contains_subject as csub ON c.course_id = csub.course_id FULL OUTER JOIN subject as s ON csub.subject_id = s.subject_id FULL OUTER JOIN offers_class as oc ON s.subject_id = oc.subject_id FULL OUTER JOIN class as cl ON oc.class_id = cl.class_id FULL OUTER JOIN meets as m ON cl.class_id = m.class_id FULL OUTER JOIN class_time as t ON m.class_time_id = t.class_time_id FULL OUTER JOIN teaches as tt ON cl.class_id = tt.class_id FULL OUTER JOIN professor as p ON tt.professor_id = p.professor_id WHERE ut.id = 1 AND e.enrollment_id = 6 AND t.class_time_id = 17 AND c.course_id = 24 AND cl.class_number = 31146'
        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)


        #Print out the course details for 595
        opt = "=============================="
        details = "Course Details"
        set_one = str(data[0][0])
        set_two = str(data[0][1])
        set_three = str(data[0][2])
        set_four = "    Class Number = " + str(data[0][3])
        set_five = "On " + str(data[0][4]) + " at " + str(data[0][5]) + " to " + str(data[0][6])
        set_six = "    Professor: " + str(data[0][7]) + " " + str(data[0][8]) + "\n" + "   Email: " + str(data[0][9])
        opt2 = "=============================="

        set_combined  = opt + "<br/><br/>" + details + "<br/><br/>" +  set_one + "<br/><br/>" + set_two + "<br/><br/>" + set_three
        set_combined2 = " " + set_four + "<br/><br/>" + set_five + "<br/><br/>" + set_six + "<br/><br/>" + opt2

        set_com = set_combined + set_combined2

        summer_2020c1 = set_com

        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(summer_2020c1))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("summer_2020c1", summer_c1)]

##==============================================================================#
##==============================================================================#
##==============================================================================#
class Action_view_summer2020_course2(Action):

    def name(self) -> Text:
        return "action_view_summer20202"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #school information slot
        summer_c2 = tracker.get_slot("summer_2020_course2")

        q = 'select  e.semester, s.subject_type, c.course_number, cl.class_number, t.day_time, t.start_time, t.end_time, p.fname, p.lname, p.email from school as sc FULL OUTER JOIN attends as a ON a.school_id = sc.school_id FULL OUTER JOIN user_type as ut ON a.id = ut.id FULL OUTER JOIN views_enrollment as ve ON ut.id = ve.id FULL OUTER JOIN enrollment as e ON ve.enrollment_id = e.enrollment_id FULL OUTER JOIN has_course as hc ON e.enrollment_id = hc.enrollment_id FULL OUTER JOIN course as c ON hc.course_id = c.course_id FULL OUTER JOIN contains_subject as csub ON c.course_id = csub.course_id FULL OUTER JOIN subject as s ON csub.subject_id = s.subject_id FULL OUTER JOIN offers_class as oc ON s.subject_id = oc.subject_id FULL OUTER JOIN class as cl ON oc.class_id = cl.class_id FULL OUTER JOIN meets as m ON cl.class_id = m.class_id FULL OUTER JOIN class_time as t ON m.class_time_id = t.class_time_id FULL OUTER JOIN teaches as tt ON cl.class_id = tt.class_id FULL OUTER JOIN professor as p ON tt.professor_id = p.professor_id WHERE ut.id = 1 AND e.enrollment_id = 6 AND t.class_time_id = 17 AND c.course_id = 25 AND cl.class_number = 31147'

        #pass the sql query to the getData method and store the results in `data` variable.
        data = getData(q)

        #Print out the course details for 595
        opt = "=============================="
        details = "Course Details"
        set_one = str(data[0][0])
        set_two = str(data[0][1])
        set_three = str(data[0][2])
        set_four = "    Class Number = " + str(data[0][3])
        set_five = "On " + str(data[0][4]) + " at " + str(data[0][5]) + " to " + str(data[0][6])
        set_six = "    Professor: " + str(data[0][7]) + " " + str(data[0][8]) + "\n" + "   Email: " + str(data[0][9])
        opt2 = "=============================="

        set_combined  = opt + "<br/><br/>" + details + "<br/><br/>" + set_one + "<br/><br/>" + set_two + "<br/><br/>" + set_three
        set_combined2 = " " + set_four + "<br/><br/>" + set_five + "<br/><br/>" + set_six + "<br/><br/>" + opt2

        set_com = set_combined + set_combined2

        summer_2020c2 = set_com

        #uttering message containing the school response from slot
        dispatcher.utter_message(text="{}".format(summer_2020c2))

        #returning the slot for school information meant for incoming graduate students
        return [SlotSet("summer_2020c2", summer_c2)]
