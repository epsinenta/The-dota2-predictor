#include "text_file_manager.h"

std::vector<std::string> TextFileManager::read(std::string filePath)
{
    rows.clear();
    std::ifstream file(filePath);
    if (!file.is_open()) {
        std::cout << "Unable to open file: " << filePath << std::endl;
        return rows;
    }
    std::string row;
    while (std::getline(file, row)) {
        rows.push_back(row);
    }
    file.close();
    return rows;
}

std::vector<std::string> TextFileManager::getRows()
{
    return rows;
}

void TextFileManager::write(std::string fileName, std::string text)
{
    std::ofstream file(fileName);

    if (file.is_open()) {
        file << text;
        file.close();
    } else {
        std::cerr << "Unable to open file " << fileName << std::endl;
    }
}

TextFileManager::~TextFileManager(){
    rows.clear();
}
