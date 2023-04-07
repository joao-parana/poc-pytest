from mypkg.upload import app
import uvicorn

if __name__ == "__main__":
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    uvicorn.run(app, host="0.0.0.0", port=8305, log_config=log_config)
