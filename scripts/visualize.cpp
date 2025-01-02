#include <SFML/Graphics.hpp>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
#include <stdexcept>

struct LogEntry
{
    std::string timestamp;
    std::string ip_address;
    std::string username;
    std::string status;
    std::string resource_accessed;
};

std::vector<LogEntry> read_csv(const std::string &filename)
{
    std::vector<LogEntry> entries;
    std::ifstream file(filename);

    if (!file.is_open())
    {
        throw std::runtime_error("Failed to open file: " + filename);
    }

    std::string line;
    std::getline(file, line); // Skip header

    while (std::getline(file, line))
    {
        LogEntry entry;
        std::stringstream ss(line);
        std::getline(ss, entry.timestamp, ',');
        std::getline(ss, entry.ip_address, ',');
        std::getline(ss, entry.username, ',');
        std::getline(ss, entry.status, ',');
        std::getline(ss, entry.resource_accessed, ',');

        if (ss.fail())
        {
            std::cerr << "Error parsing line: " << line << std::endl;
            continue;
        }

        entries.push_back(entry);
    }

    return entries;
}

void visualize_data_flow(const std::vector<LogEntry> &logs)
{
    // Simple text-based visualization
    for (const auto &entry : logs)
    {
        std::cout << entry.timestamp << " - "
                  << entry.ip_address << " - "
                  << entry.username << " - "
                  << entry.status << " - "
                  << entry.resource_accessed << std::endl;
    }
}

int main()
{
    try
    {
        std::vector<LogEntry> web_logs = read_csv("datasets/web_server_logs.csv");
        visualize_data_flow(web_logs);
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}