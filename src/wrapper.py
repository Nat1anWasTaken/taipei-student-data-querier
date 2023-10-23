class TaipeiStudentDataQuerier:
    """
    A class used to query student data from Taipei City School Administration System
    """

    def __init__(self, session_id: str):
        """
        Initializes a new instance of the class.

        Args:
            session_id (str): The ID of the session to use for the wrapper.
        """
        self.session_id: str = session_id

    def fetch_absence_data(self) -> dict:
        """
        Gets the absence data of the student.

        Returns:
            dict: The absence data of the student.
        """
        pass
