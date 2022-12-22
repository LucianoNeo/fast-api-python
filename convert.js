const ffmpeg = require("fluent-ffmpeg");

ffmpeg()
  .input("testes/audio.mp3")
  .output("output.wav")
  .on("end", () => {
    console.log("Conversion completed!");
  })
  .run();
