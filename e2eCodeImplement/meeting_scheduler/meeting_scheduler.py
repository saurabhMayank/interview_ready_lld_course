from enum import Enum
import time
from abc import ABC, abstractmethod
from typing import List

from datetime import datetime, timedelta


class MeetingModel:
    # time tuple -> (hrs, mins) 
    # same for duration
    def __init__(self, name, meeting_time: tuple, duration: tuple):
        self.id = time.time()
        self.name = name
        self.meeting_time = meeting_time
        # duration in hrs
        self.duration = duration


class RoomModel:
    def __init__(self, name):
        self.id = time.time()
        self.name = name


class UserModel:
    def __init__(self, name, email):
        self.id = time.time()
        self.email = email
        self.name = name


class MeetingSchedulerModel:
    total_meeting_transaction = []

    # signify row in the DB
    def __init__(self, user: UserModel, meeting: MeetingModel, room: RoomModel):
        self.id = time.time()
        self.user = user
        self.meeting = meeting
        self.room = room

    @staticmethod
    def add_meeting_transac_to_total(meeting_transac_obj):
        MeetingSchedulerModel.total_meeting_transaction.append(meeting_transac_obj)


"""
Services
"""


class MeetingService:
    def __init__(self):
        pass

    def get_meeting_list(self, meeting_id: int):
        """
        Function api to get meeting by meeting id
        """

        # valdiation of meeting_id
        
        meeting_list = []
        for meeting_sch_obj in MeetingSchedulerModel.total_meeting_transaction:
            if meeting_sch_obj.meeting.id == meeting_id:
                meeting_list.append(meeting_sch_obj.meeting)
        
        return meeting_list


class UserService:
    def __init__(self):
        pass
    
    def add_user(self, name: str, email: str):
        """
        Functional API to add User
        Responsibility
        -> Do all the validation
        -> Have some wrapper logic
        Before adding User to the DB (UserModel)
        """

        if not isinstance(name, str):
            raise Exception("user_name should be string")

        # similar validation check for email

        user_model_obj = UserModel(name, email)
        return user_model_obj


    def get_meeting_list(self, user_name: str):
        """
         Function api to get meeting by user_name
        """

        # valdiation of user_name
        
        meeting_list = []
        for meeting_sch_obj in MeetingSchedulerModel.total_meeting_transaction:
            if meeting_sch_obj.user.name == user_name:
                meeting_list.append(meeting_sch_obj.meeting)
        
        return meeting_list



class RoomService:
    def __init__(self):
        pass
    

    def add_room(self, name: str):
        """
        Functional API to add room
        Responsibility
        -> Do all the validation
        -> Have some wrapper logic
        Before adding User to the DB (UserModel)
        """

        if not isinstance(name, str):
            raise Exception("user_name should be string")

        # similar validation check for email

        room_model_obj = RoomModel(name)
        return room_model_obj

    def get_meeting_list(self, room_name: int):
        """
        Function api to get meeting by room_name
        """

        # valdiation of meeting_id
        
        meeting_list = []
        for meeting_sch_obj in MeetingSchedulerModel.total_meeting_transaction:
            if meeting_sch_obj.room.name == room_name:
                meeting_list.append(meeting_sch_obj.meeting)
        
        return meeting_list



class MeetingSchedulerService:
    def __init__(self):
        pass

    def schedule_meeting(
        self,
        user_list: List[UserModel],
        room: RoomModel,
        time: tuple,
        duration: tuple,
        meeting_name: str,
    ):
        """
        Functional API to schedule meeting
        Checks
        -> Check if at that time -> room available or not
        -> check if all users available at that time
        -> if there is any conflict -> suggest another time slot
        -> Else schedule the meeting

        -> Extension -> Suggest another slot if conflict (not implemented)
        """

        # meeting start time
        start_time = time
        end_time = (time[0]+duration[0], time[1]+duration[1])

        # check if room available
        for meeting_sch_obj in MeetingSchedulerModel.total_meeting_transaction:
            if (
                room.id == meeting_sch_obj.room.id
                and meeting_sch_obj.meeting.meeting_time[0]+ meeting_sch_obj.meeting.duration[0] > start_time[0]
            ):
                # room matches the room id 
                # and there is meeting scheduled at that time in that room
                # scheduled_meeting_time + duration > curr_meet_start_time 
                # then curr_meeting cannot be scheduled in same room
                raise Exception("Room is not available in that time")

        # check if all users are free
        for meeting_sch_obj in MeetingSchedulerModel.total_meeting_transaction:
            if (
                meeting_sch_obj.user in user_list
                and meeting_sch_obj.meeting.meeting_time[0] + meeting_sch_obj.meeting.duration[0] > start_time[0]
            ):
                # if user has scheduled meetings
                # and
                # scheduled_meeting_time + duration > curr_meet_start_time 
                # then meeting_sch_obj.user cannot join curr_meeting
                raise Exception(
                    f"User {meeting_sch_obj.user.name} not available at the defined, pls choose another time"
                )

        # schedule the meeting
        meeting_obj = MeetingModel(meeting_name, time, duration)
        for user_obj in user_list:
            meeting_sch_obj = MeetingSchedulerModel(user_obj, meeting_obj, room)
            MeetingSchedulerModel.add_meeting_transac_to_total(meeting_sch_obj)

        
        print("Meeting is scheduled")


"""
Api Handler
"""
class ApiHandler:
    def __init__(self):
        pass
    
    def add_user(self, name, email):
        user_service = UserService()

        user_obj = user_service.add_user(name, email)
        return user_obj
    
    def add_room(self, name):

        room_service = RoomService()
        room_obj = room_service.add_room(name)
        return room_obj


    def schedule_meeting(self, user_list, room, time, duration, meeting_name):
        meeting_sch = MeetingSchedulerService()
        meeting_sch.schedule_meeting(user_list, room, time, duration, meeting_name)


def main():
    """
    """
    api_handler = ApiHandler()

    user1_obj = api_handler.add_user("mayank", "mayank@abc.com")

    user2_obj = api_handler.add_user("saurabh", "saurabh@abc.com")


    user3_obj = api_handler.add_user("saurabh", "saurabh@abc.com")

    room1_obj = api_handler.add_room("sushruta")
    room2_obj = api_handler.add_room("ramanujan")
    room3_obj = api_handler.add_room("chanakya")



    # time is 24 hours clock here
    # elements of tuple will be int
    # time is provided in tuple (hrs, mins)
    # meeting duration in tuple (hrs, mins)
    # only hrs will be updated minutes will be 0 for now

    # case 1 -> schedule meeting
    time = (16, 00)
    duration = (1, 00)
    api_handler.schedule_meeting([user1_obj, user2_obj], room1_obj, time, duration, "random_meet")


    # case 2 -> try to schedule meeting at same time in a different room
    # time = (16, 00)
    # duration = (1, 00)
    # # schedule_meeting(user_list, room, time, duration, meeting_name)
    # api_handler.schedule_meeting([user1_obj, user2_obj], room2_obj, time, duration, "random_meet_2")

    # case 3 -> trying to schedule meeting at different time in same room
    # time = (17, 00)
    # duration = (1, 00)
    # # schedule_meeting(user_list, room, time, duration, meeting_name)
    # api_handler.schedule_meeting([user1_obj, user2_obj], room1_obj, time, duration, "random_meet_2")

    # case 4 -> adding a user whose meeting is already booked that time
    time = (16, 00)
    duration = (1, 00)
    # schedule_meeting(user_list, room, time, duration, meeting_name)
    api_handler.schedule_meeting([user1_obj, user3_obj], room3_obj, time, duration, "random_meet_3")




if __name__ == "__main__":
    main()
