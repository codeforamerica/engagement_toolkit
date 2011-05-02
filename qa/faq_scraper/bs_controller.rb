require "./bing_scrape.rb"
key = "248A1D8594169FE22B8F3D5BDB8F6C19141FD2F5"
ts = Time.now.strftime("%Y%m%d_%H%M%S")

#domains = ['phila.gov','seattle.gov']
terms = ['faq','frequently asked questions']

terms.each do |t| 
  BingScraper.new('phila.gov',key,t,"/Users/mertonium/Code/engagement_toolkit/qa/faq_scraper/bing_results","PHL_#{ts}")
end

terms.each do |t| 
  BingScraper.new('seattle.gov', key,t,"/Users/mertonium/Code/engagement_toolkit/qa/faq_scraper/bing_results","SEA_#{ts}")
end
