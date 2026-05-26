import joblib
import pandas as pd
from fastapi import APIRouter
from pydantic import BaseModel, Field

from api.config import MODEL_PATH
from api.logger import logger

router = APIRouter(
    prefix="/ml-prediction",
)


class PredictionInput(BaseModel):
    Quantity: int = Field(
        ...,
        json_schema_extra={
            "example": 3
        }
    )
    Discount: float = Field(
        ...,
        json_schema_extra={
            "example": 0.0
        }
    )
    Profit: float = Field(
        ...,
        json_schema_extra={
            "example": 120.50
        }
    )


@router.post("", summary="ML Prediction")
def ml_prediction(data: PredictionInput):
    try:
        logger.info("ML prediction request received")

        if not MODEL_PATH.exists():
            return {
                "status": "failed",
                "message": f"Model file not found: {MODEL_PATH}"
            }

        model = joblib.load(MODEL_PATH)

        input_data = pd.DataFrame(
            [
                {
                    "Quantity": data.Quantity,
                    "Discount": data.Discount,
                    "Profit": data.Profit
                }
            ],
            columns=["Quantity", "Discount", "Profit"]
        )

        prediction = model.predict(input_data)

        return {
            "status": "success",
            "message": "Prediction generated successfully",
            "input_features": {
                "Quantity": data.Quantity,
                "Discount": data.Discount,
                "Profit": data.Profit
            },
            "predicted_sales": float(prediction[0])
        }

    except Exception as error:
        logger.error(f"ML prediction failed: {error}")

        return {
            "status": "failed",
            "message": str(error),
            "hint": "This model was trained using Quantity, Discount and Profit in the same order."
        }
