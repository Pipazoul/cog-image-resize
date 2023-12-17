# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor, Input, Path
from PIL import Image


class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        # self.model = torch.load("./weights.pth")

    def predict(
        self,
        image: Path = Input(description="Input image"),
        width: int = Input(description="Width of the output image", default=512),
        height: int = Input(description="Height of the output image", default=512),
    ) -> Path:
        """Run a single prediction on the model"""
        toCropImage = Image.open(image)
        toCropImage.thumbnail((width, height))
        toCropImage.save("test.png")

        return Path("test.png")

