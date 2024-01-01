#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <filesystem>
namespace fs = std::__fs::filesystem;

std::vector<std::string> split(const std::string &s, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    while (std::getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

void combineCSVFiles(const std::vector<std::string>& filePaths, const std::string& outputFilePath) {
    std::ofstream outputFile(outputFilePath);
    bool firstFile = true;

    for (const auto& filePath : filePaths) {
        std::ifstream file(filePath);
        std::string line;

        if (file.is_open()) {
            // Skip the header line for all but the first file
            if (!firstFile) std::getline(file, line);

            while (std::getline(file, line)) {
                outputFile << line << std::endl;
            }
            file.close();

            firstFile = false;
        } else {
            std::cout << "Unable to open file: " << filePath << std::endl;
        }
    }

    outputFile.close();
}

int main() {
    std::string path = "../data"; // Path to the directory
    std::vector<std::string> csvFiles;

    // Iterate over the directory and subdirectories
    for (const auto& entry : fs::recursive_directory_iterator(path)) {
        if (entry.is_regular_file() && entry.path().extension() == ".csv") {
            csvFiles.push_back(entry.path().string());
        }
    }

    // Combine CSV files into one
    std::string outputPath = "../data/combined.csv";
    combineCSVFiles(csvFiles, outputPath);

    return 0;
}
