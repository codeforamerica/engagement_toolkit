require "./bing_scrape.rb"
key = "248A1D8594169FE22B8F3D5BDB8F6C19141FD2F5"
ts = Time.now.strftime("%Y%m%d_%H%M%S")
path = "/Users/mertonium/Code/engagement_toolkit/qa/faq_scraper/bing_results"

#domains = ['phila.gov','seattle.gov']
terms = ['faq','frequently asked questions']

phl = BingScraper.new('phila.gov',key,path,"PHL_#{ts}")
terms.each do |t| 
  phl.scrape_bing(t)
end
phl.create_file

sea = BingScraper.new('seattle.gov',key,path,"SEA_#{ts}")
terms.each do |t| 
  sea.scrape_bing(t)
end
sea.create_file
