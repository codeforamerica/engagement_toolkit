require "./bing_scrape.rb"

# Setup config vars
key = "248A1D8594169FE22B8F3D5BDB8F6C19141FD2F5"
ts = Time.now.strftime("%Y%m%d_%H%M%S")
path = "/Users/mertonium/Code/engagement_toolkit/qa/faq_scraper/bing_results"

# Set our search terms
terms = ['faq','frequently asked questions']

# Philadelphia
phl = BingScraper.new('phila.gov',key,path,"PHL_#{ts}")
terms.each do |t| 
  phl.scrape_bing(t)
end
phl.create_file

# Seattle
sea = BingScraper.new('seattle.gov',key,path,"SEA_#{ts}")
terms.each do |t| 
  sea.scrape_bing(t)
end
sea.create_file

# San Francisco
# Example of using multiple domains for one city
sfdomains = ['sfgov.org','sfgov2.org','sfdpw.org','sfenvironment.org','sfrecycling.com','sfdph.org','sfredevelopment.org']
sf = BingScraper.new('sfgov2.org',key,path,"SF_#{ts}")
sfdomains.each do |sfd|
  sf.domain = sfd
  terms.each do |t| 
    sf.scrape_bing(t)
  end
end
sf.create_file