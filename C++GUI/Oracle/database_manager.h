#ifndef DATABASE_MANAGER_H
#define DATABASE_MANAGER_H

#include <libpq-fe.h>
#include <String>
#include <Vector>
#include <Map>

class DataBaseManager
{
private:
    std::string password;
    std::string user;
    std::string database_name;
    std::string host;
    std::string port;

public:
    DataBaseManager(std::string _database_name) ;
    DataBaseManager() ;
    ~DataBaseManager();
    void setDataBaseName(std::string _database_name);
    void readParams();
    std::vector<std::vector<std::string>> getRows(std::string table_name, std::map<std::string, std::string> args);
    std::vector<std::vector<std::string>> getFullTable(std::string table_name);
};

#endif // DATABASE_MANAGER_H
