# _______________________________________
# for LOGGING:

# from src.logger import logging
# logging.debug("this is a demo debug")
# _______________________________________


# _______________________________________
# for EXCEPTION:

# from src.logger import logging
# from src.exception import MyException
# import sys
# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e
# _______________________________________


# _________________________________________________________________
# for DATA INGESTION, VALIDATION, TRANSFORMATION, MODEL TRAINING:

from src.pipline.training_pipeline import TrainPipeline
pipeline = TrainPipeline()
pipeline.run_pipeline()
# _________________________________________________________________


# mongodb+srv://Achyuth_mlops_user:Iu6mo7qIJmqRnfAU@cluster0.72vxxxt.mongodb.net/?appName=Cluster0

# new username:  Achyuth
# new pswd:      SUItvUHbmRqNVJdM
# mongodb+srv://Achyuth:SUItvUHbmRqNVJdM@cluster0.72vxxxt.mongodb.net/?appName=Cluster0