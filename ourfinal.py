import unittest
from datetime import datetime

class Appointment:
    def __init__(self, athlete_id, datetime):
        self.athlete_id = athlete_id
        self.datetime = datetime
        self.feedback = None

class AppointmentSystem:
    def __init__(self):
        self.appointments = {}

    def create_appointment(self, athlete_id, datetime):
        appointment = Appointment(athlete_id, datetime)
        self.appointments[athlete_id] = appointment

    def get_appointment(self, athlete_id):
        return self.appointments.get(athlete_id)

    def update_appointment(self, athlete_id, new_datetime):
        if athlete_id in self.appointments:
            self.appointments[athlete_id].datetime = new_datetime
            return True
        return False

    def delete_appointment(self, athlete_id):
        if athlete_id in self.appointments:
            del self.appointments[athlete_id]
            return True
        return False

    def schedule_sport_psychology_sessions(self, athlete_id, datetime):
        self.create_appointment(athlete_id, datetime)

    def manage_session_feedback(self, athlete_id, feedback_data):
        if athlete_id in self.appointments:
            self.appointments[athlete_id].feedback = feedback_data
            return True
        return False

class TestAppointmentSystem(unittest.TestCase):
    def setUp(self):
        self.appointment_system = AppointmentSystem()

    def test_create_appointment(self):
        self.appointment_system.create_appointment(1, datetime(2024, 4, 29, 10, 0))
        appointment = self.appointment_system.get_appointment(1)
        self.assertIsNotNone(appointment)

    def test_update_appointment(self):
        self.appointment_system.create_appointment(1, datetime(2024, 4, 29, 10, 0))
        self.assertTrue(self.appointment_system.update_appointment(1, datetime(2024, 4, 30, 11, 0)))
        appointment = self.appointment_system.get_appointment(1)
        self.assertEqual(appointment.datetime, datetime(2024, 4, 30, 11, 0))

    def test_delete_appointment(self):
        self.appointment_system.create_appointment(1, datetime(2024, 4, 29, 10, 0))
        self.assertTrue(self.appointment_system.delete_appointment(1))
        appointment = self.appointment_system.get_appointment(1)
        self.assertIsNone(appointment)

    def test_schedule_sport_psychology_sessions(self):
        self.appointment_system.schedule_sport_psychology_sessions(1, datetime(2024, 4, 29, 10, 0))
        appointment = self.appointment_system.get_appointment(1)
        self.assertIsNotNone(appointment)

    def test_manage_session_feedback(self):
        self.appointment_system.create_appointment(1, datetime(2024, 4, 29, 10, 0))
        self.assertTrue(self.appointment_system.manage_session_feedback(1, "Great session!"))
        appointment = self.appointment_system.get_appointment(1)
        self.assertEqual(appointment.feedback, "Great session!")

if __name__ == '__main__':
    unittest.main(verbosity=2)
