#include "text_file_reader.h"

std::vector<std::string> TextFileReader::read(std::string filePath)
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

std::vector<std::string> TextFileReader::getRows()
{
    return rows;
}

TextFileReader::~TextFileReader(){
    rows.clear();
}
