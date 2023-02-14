document.getElementById("filesForm").reset();

const fileNames = document.getElementById("id_fileNames");

const inputFiles = document.getElementById("mp3FileInput")

inputFiles.addEventListener("change", function () {
    let files = this.files;
    for (let i = 0; i < files.length; i++) {
        const fileName = files[i].name;
        fileNames.value += fileName + ","
    }
});