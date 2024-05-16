#ifndef TEXTFILEMANAGER_H
#define TEXTFILEMANAGER_H

#include <Vector>
#include <String>
#include <fstream>
#include <iostream>

class TextFileManager{
private:
    std::vector<std::string> rows;
public:
    TextFileManager(){};
    ~TextFileManager();
    std::vector<std::string> read(std::string filePath);
    std::vector<std::string> getRows();
    void write(std::string fileName, std::string text);
};

#endif // TEXTFILEMANAGER_H
