#include "database_manager.h"
#include "text_file_reader.h"

DataBaseManager::DataBaseManager()
{
    readParams();
}

DataBaseManager::DataBaseManager(std::string _database_name) : DataBaseManager::DataBaseManager()
{
    database_name = _database_name;
}

void DataBaseManager::readParams()
{
    //std::vector<std::string> params = TextFileReader().read("./config.txt");
    user = "postgres";
    password = "1q2ws3edc4r";
    host = "127.0.0.1";
    port = "5432";
}

void DataBaseManager::setDataBaseName(std::string _database_name)
{
    database_name = _database_name;
}

DataBaseManager::~DataBaseManager()
{
    password.clear();
    user.clear();
    database_name.clear();
    host.clear();
    port.clear();
}

std::vector<std::vector<std::string>> DataBaseManager::getRows(std::string table_name, std::map<std::string, std::string> args)
{
    std::string connInfoString = "dbname = " + database_name + " user = " + user + " password = " + password + " hostaddr = " + host + " port = " + port;
    const char * conninfo = connInfoString.c_str();

    PGconn *conn = PQconnectdb(conninfo);

    if (PQstatus(conn) != CONNECTION_OK) {
        fprintf(stderr, "Ошибка подключения: %s", PQerrorMessage(conn));
        PQfinish(conn);
        exit(1);
    }

    std::string request = "SELECT * FROM " + table_name + " WHERE ";
    for(auto iter{args.begin()}; iter != args.end(); iter++){
        request +=  iter->first + " = '" + iter->second + "'";
        if (std::next(iter) != args.end()) {
            request += " AND ";
        }
    }

    request += ";";
    std::cout << request << '\n';
    PGresult *res = PQexec(conn, request.c_str());

    if (PQresultStatus(res) != PGRES_TUPLES_OK) {
        fprintf(stderr, "Error: %s", PQerrorMessage(conn));
        PQclear(res);
        PQfinish(conn);
        exit(1);
    }


    int rows = PQntuples(res);
    int cols = PQnfields(res);
    std::vector<std::vector<std::string>> result;
    for (int i = 0; i < rows; i++) {
        std::vector<std::string> buf;
        for(int j = 0; j < cols; j++)
            buf.push_back(PQgetvalue(res, i, j));
        result.push_back(buf);
    }

    PQclear(res);
    PQfinish(conn);

    return result;

}
std::vector<std::vector<std::string>> DataBaseManager::getFullTable(std::string table_name)
{
    std::string connInfoString = "dbname = " + database_name + " user = " + user + " password = " + password + " hostaddr = " + host + " port = " + port;
    const char * conninfo = connInfoString.c_str();

    PGconn *conn = PQconnectdb(conninfo);

    if (PQstatus(conn) != CONNECTION_OK) {
        fprintf(stderr, "Ошибка подключения: %s", PQerrorMessage(conn));
        PQfinish(conn);
        exit(1);
    }


    std::string request = "SELECT * FROM " + table_name;

    std::cout << request << '\n';
    PGresult *res = PQexec(conn, request.c_str());

    if (PQresultStatus(res) != PGRES_TUPLES_OK) {
        fprintf(stderr, "Error: %s", PQerrorMessage(conn));
        PQclear(res);
        PQfinish(conn);
        exit(1);
    }


    int rows = PQntuples(res);
    int cols = PQnfields(res);
    std::vector<std::vector<std::string>> result;
    for (int i = 0; i < rows; i++) {
        std::vector<std::string> buf;
        for(int j = 0; j < cols; j++)
            buf.push_back(PQgetvalue(res, i, j));
        result.push_back(buf);
    }

    PQclear(res);
    PQfinish(conn);

    return result;

}
