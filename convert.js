const ffmpeg = require("fluent-ffmpeg");

ffmpeg()
  .input("teste/audio.mp3")
  .output("output.wav")
  .on("end", () => {
    console.log("Conversion completed!");
  })
  .run();
