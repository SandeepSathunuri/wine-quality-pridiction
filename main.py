from mlProject.utils import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainigPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTainerTainingPipepine
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationtainingPipeline

logger.info("Welcome to mlproject")

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\n==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion=DataValidationTrainigPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\n==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation stage"
try:
    logger.info(f">>>>>>>>>{STAGE_NAME}<<<<<<<")
    data_ingestion=DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed<<<<<<<<<<<\n\n=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Training stage"
try:
    logger.info(f">>>>>>>>>{STAGE_NAME}<<<<<<<<<")
    data_ingestion=ModelTainerTainingPipepine()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>>>{STAGE_NAME}<<<<<<<<<<<\n\n==============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Evaluation stage"
try:
    logger.info(f">>>>>>>>>{STAGE_NAME}<<<<<<<<<")
    data_ingestion=ModelEvaluationtainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>>>{STAGE_NAME}<<<<<<<<<<<\n\n==============x")
except Exception as e:
    logger.exception(e)
    raise e