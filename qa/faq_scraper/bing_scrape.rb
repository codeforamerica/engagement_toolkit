require 'CSV'
require 'rbing'
require 'time'


class BingScraper

  # @params domain is a non subdomained entity such as phila.gov
  # @params key is the bing key
  # @params file path is the root path for the file
  # @params file name does not iunclude csv
  # @params query is a string for the actual query such as "Frequently Asked Questions"  
  def initialize(domain, key, query, file_path, file_name)
    @domain = domain
    @query = query
    @file_name = file_name
    @file_path = file_path
    @bing = RBing.new(key)
    scrape_bing
    create_file
  end
    
  def scrape_bing
    @g = []
    a = 0
    # Only allows 1000 results, which is 20 pages * 50 results per page
    while a != 20
      rsp = @bing.web('(site:'+@domain+') "' + @query +'"', {:count => 50, :offset => a})
      rsp["Web"]["Results"].each do |x|
        @g << x["Url"]
      end
      a = a + 1
      # puts a
    end

    exclusion = ""
    @g.uniq[0..20].map { |x| exclusion = exclusion + ' -"' + x +'"'}
    a = 0
    # puts exclusion
    while a != 20
      rsp = @bing.web('(site:'+@domain+') "Frequently Asked Questions"' + exclusion, {:count => 50, :offset => a})
      rsp["Web"]["Results"].each do |x|
        @g << x["Url"] unless @g.include?(x["Url"])
      end
      a = a + 1
      # puts a
    end


  end

  def create_file
    CSV.open(@file_path + "/" + @file_name + ".csv", "a") do |csv|
      @g.uniq.each do |x|
        csv << [x]
      end
    end
    return @file_path + "/" +@file_name + ".csv"
  end

end