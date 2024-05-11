#ifndef TEXT_FILE_READER_H
#define TEXT_FILE_READER_H

#include <Vector>
#include <String>
#include <fstream>
#include <iostream>

class TextFileReader{
private:
    std::vector<std::string> rows;
public:
    TextFileReader(){};
    ~TextFileReader();
    std::vector<std::string> read(std::string filePath);
    std::vector<std::string> getRows();
};

#endif // TEXT_FILE_READER_H
