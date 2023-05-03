from roboflow import Roboflow

rf = Roboflow(api_key="dCtQn80N56V8fZxHLgPv")
project = rf.workspace().project("sem-ii-v2-1")
model = project.version(1).model

# infer on a local image
path = input("enter image path for image inference: ")
print(model.predict(path).json())
#model.predict(path).save(f"prediction_{path}.jpg")
model.predict(path).plot()