import sys,os



class InsurancsException(Exception):


    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = InsurancsException.error_message_detail(error_message, error_detail=error_detail)

    @staticmethod
    def error_message_detail(error: Exception, error_detail: sys)->str:
        _, _, exc_tb = error_detail.exc_info()

        #extracting file name from exception traceback
        file_name = exc_tb.to_frame.f_code.co_filename

        #preparing error message
        error_message = f"Error occured python script name [{file_name}]"\
                        f" line numer [{exc_tb.tb_lineno}] error message [{error}]."


        return error_message

    def __str__(self):
        return InsurancsException.__name__.__str__()
