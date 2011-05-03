require 'CSV'
require 'rbing'
require 'time'


class BingScraper
  # Allow domain to be accessed
  attr_accessor :domain
  
  # @params domain is a non subdomained entity such as phila.gov
  # @params key is the bing key
  # @params file path is the root path for the file
  # @params file name does not iunclude csv
  def initialize(domain, key, file_path, file_name)
    @domain = domain
    @query = ''
    @file_name = file_name
    @file_path = file_path
    @bing = RBing.new(key)
    @data_store = []
  end
  
  # @params query is a string for the actual query such as "Frequently Asked Questions"  
  def scrape_bing(query)
    @query = query
    @g = []
    a = 0
    # Only allows 1000 results, which is 20 pages * 50 results per page
    while a != 20
      rsp = @bing.web('(site:'+@domain+') "' + @query +'"', {:count => 50, :offset => a})
      if !rsp["Web"]["Results"].nil?
        rsp["Web"]["Results"].each do |x|
          @g << x["Url"]
        end
      end 
      a = a + 1
    end

    exclusion = ""
    @g.uniq[0..20].map { |x| exclusion = exclusion + ' -"' + x +'"'}
    a = 0

    while a != 20
      rsp = @bing.web('(site:'+@domain+') "' + @query + '" ' + exclusion, {:count => 50, :offset => a})
      if !rsp["Web"]["Results"].nil?
        rsp["Web"]["Results"].each do |x|
          @g << x["Url"] unless @g.include?(x["Url"])
        end
      end
      a = a + 1
    end
    
    @data_store = @data_store | @g
  end

  def create_file
    CSV.open(@file_path + "/" + @file_name + ".csv", "w") do |csv|
      csv << ['url']
      @data_store.uniq.each do |x|
        csv << [x]
      end
    end
    return @file_path + "/" +@file_name + ".csv"
  end

end