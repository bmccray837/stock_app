import yfinance as yf

russell3000 = ['TXG', 'FLWS', 'ONEM', 'SRCE', 'XXII', 'TWOU', 'DDD', 'MMM', 'FDMT', 'ETNB', 'EGHT', 'NMTR', 'MASS', 'ATEN', 'AAON', 'AIR', 'ABT', 'ABBV', 'ANF', 'ABMD', 'ABM', 'ACTG', 'ASO', 'ACHC', 'ACAD', 'AKR', 'ACEL', 'AXDX', 'XLRN', 'ACN', 'ACCO', 'ACCD', 'RCM', 'ARAY', 'ACIW', 'ACRS', 'ATVI', 'AYI', 'GOLF', 'AFIB', 'AHCO', 'ADPT', 'ADUS', 'ACET', 'ADNT', 'ADBE', 'ADT', 'ATGE', 'ADTN', 'AAP', 'WMS', 'AEIS', 'AMD', 'ASIX', 'ADV', 'ADN', 'ADVM', 'ACM', 'AGLE', 'AMTX', 'AERI', 'AJRD', 'AVAV', 'ASLE', 'AES', 'AEVA', 'AFCG', 'AMG', 'AFMD', 'AFL', 'AGCO', 'UAVS', 'AGEN', 'A', 'AGTI', 'AGL', 'AGYS', 'AGIO', 'AGNC', 'ADC', 'AL', 'APD', 'ATSG', 'AKAM', 'AKBA', 'AKRO', 'AKUS', 'AKTS', 'AKYA', 'ALG', 'ALRM', 'ALK', 'AIN', 'ALB', 'ACI', 'ALBO', 'AA', 'ALDX', 'ALEC', 'ALRS', 'ALEX', 'ALX', 'ARE', 'ALXN', 'ALGN', 'ALHC', 'ALGS', 'ALKT', 'ALKS', 'ALLK', 'Y', 'ATI', 'ABTX', 'ALGT', 'ALLE', 'ALGM', 'ALE', 'ADS', 'LNT', 'AMOT', 'ALSN', 'ALLO', 'ALVR', 'MDRX', 'ALL', 'ALLY', 'ALNY', 'AOSL', 'GOOGL', 'GOOG', 'ATEC', 'ALPN', 'ALTG', 'ALTA', 'ALTR', 'AYX', 'ATUS', 'ALT', 'ALTO', 'AIMC', 'MO', 'ALTM', 'ALXO', 'AMAL', 'AMZN', 'AMBC', 'AMBA', 'AMC', 'AMCX', 'AMCR', 'DOX', 'AMED', 'AMTB', 'UHAL', 'AEE', 'AMRC', 'CRMT', 'AAL', 'AAT', 'AXL', 'ACC', 'AEO', 'AEP', 'AEL', 'AXP', 'AFG', 'AFIN', 'AMH', 'AIG', 'AMNB', 'ANAT', 'AOUT', 'APEI', 'AMSWA', 'AWR', 'AMSC', 'AMT', 'AVD', 'AWK', 'AMWL', 'AMWD', 'COLD', 'AMP', 'ABCB', 'AMSF', 'ABC', 'AME', 'AMGN', 'FOLD', 'AMKR', 'POWW', 'AMN', 'AMRK', 'AMPH', 'APH', 'AMPE', 'AMRS', 'ADI', 'PLAN', 'ANAB', 'AVXL', 'ANDE', 'ANGO', 'ANGN', 'ANIP', 'ANIK', 'NLY', 'ANNX', 'ANSS', 'ATRS', 'ATEX', 'AM', 'AR', 'ANTM', 'AON', 'APA', 'AIRC', 'AIV', 'APLS', 'APG', 'APOG', 'ARI', 'APO', 'AMEH', 'APPF', 'APPH', 'APPN', 'APLE', 'AAPL', 'AIT', 'AMAT', 'AMTI', 'APLT', 'APR', 'ATR', 'APTV', 'APYX', 'AQB', 'ARMK', 'ABR', 'AMRX', 'ACGL', 'ARCH', 'ADM', 'AROC', 'FUV', 'ARNC', 'ACA', 'ARCT', 'RCUS', 'ARQT', 'ARD', 'ARDX', 'ARNA', 'ACRE', 'ARES', 'AGX', 'ARGO', 'ANET', 'ARKO', 'ARLO', 'AHH', 'ARR', 'AWI', 'ARRY', 'ARW', 'AROW', 'ARWR', 'ARTNA', 'AJG', 'APAM', 'ARVN', 'ASAN', 'ABG', 'ASXC', 'ASGN', 'AHT', 'ASH', 'ASPN', 'AZPN', 'AWH', 'AMK', 'ASB', 'AC', 'AIZ', 'AGO', 'ASTE', 'ATRO', 'ABUS', 'ARCB', 'ATRA', 'AVIR', 'ATER', 'ATH', 'ATNX', 'ATHX', 'ATHA', 'ATKR', 'ACBI', 'AUB', 'ATLC', 'AAWW', 'ATCX', 'TEAM', 'ATO', 'ATNI', 'ATOM', 'ATOS', 'BCEL', 'ATRC', 'ATRI', 'AUD', 'ADSK', 'ADP', 'AN', 'AZO', 'AVLR', 'AVB', 'AGR', 'AVNS', 'AVTR', 'AVYA', 'AVAH', 'AVY', 'AVNW', 'CDMO', 'AVID', 'RNA', 'AVNT', 'CAR', 'AVA', 'RCEL', 'AVT', 'AVRO', 'AXTA', 'ACLS', 'HOME', 'T', 'AXNX', 'AX', 'AXSM', 'AXTI', 'AZZ', 'RILY', 'BGS', 'BW', 'BMI', 'BKR', 'BCPC', 'BLL', 'BALY', 'BANC', 'BANF', 'BLX', 'BXS', 'BAND', 'BFC', 'BAC', 'BOH', 'BMRC', 'NTB', 'BK', 'OZK', 'BKU', 'BANR', 'BHB', 'BNED', 'B', 'BBSI', 'BSET', 'BAX', 'BECN', 'BEEM', 'BEAM', 'SKIN', 'BZH', 'BDX', 'BBBY', 'BDC', 'BRBR', 'BHE', 'BNFT', 'BSY', 'BLI', 'AXS', 'AXGN', 'AXON', 'BRY', 'BERY', 'BBY', 'BYND', 'BYSI', 'BGCP', 'BGFV', 'BIG', 'BIGC', 'BH', 'BILL', 'BCAB', 'BCRX', 'BDSI', 'BDSX', 'BIIB', 'BHVN', 'BLFS', 'BMRN', 'BMEA', 'BNGO', 'BIO', 'TECH', 'BVS', 'BTAI', 'BJRI', 'BJ', 'BDTX', 'BKH', 'BKI', 'BLKB', 'BL', 'BLK', 'BXMT', 'BLNK', 'HRB', 'BE', 'BLMN', 'BCOR', 'BLBD', 'BRBS', 'BLUE', 'BVH', 'BXC', 'BPMC', 'WRB', 'BRK.B', 'BHLB', 'BCEI', 'BKNG', 'BOOT', 'BAH', 'BWA', 'SAM', 'BOMN', 'BPFH', 'BXP', 'BSX', 'EPAY', 'BOX', 'BYD', 'BRC', 'BHR', 'BDN', 'BBIO', 'BWB', 'MNRL', 'BFAM', 'BCOV', 'BHF', 'BSIG', 'BRSP', 'BV', 'EAT', 'BCO', 'BMY', 'VTOL', 'BRX', 'AVGO', 'BRMK', 'BR', 'BNL', 'BKD', 'BIPC', 'BPYU', 'BEPC', 'BRKL', 'BTX', 'BRKS', 'BRO', 'BF.B', 'BF.A', 'BRP', 'BA', 'BCC', 'BOKF', 'BOLT', 'BTRS', 'BKE', 'BLDR', 'BG', 'BURL', 'BFST', 'BFLY', 'BWXT', 'BY', 'BYRN', 'CHRW', 'AI', 'CCCC', 'CABO', 'CBT', 'COG', 'CACI', 'WHD', 'CADE', 'CDNS', 'CDZI', 'CZR', 'CSTE', 'CAI', 'CAMP', 'CVGW', 'CAL', 'CRC', 'CWT', 'CALX', 'ELY', 'CPE', 'CALM', 'CMBM', 'CATC', 'CAC', 'CPT', 'CPB', 'CWH', 'CNNE', 'GOEV', 'CTLP', 'CBNK', 'CCBG', 'BRT', 'BRKR', 'BC', 'BMTC', 'CARA', 'CRDF', 'CAH', 'CSII', 'CDLX', 'CDNA', 'CTRE', 'CARG', 'CSL', 'LOTZ', 'CG', 'KMX', 'CCL', 'PRTS', 'CRS', 'CSV', 'CARR', 'TAST', 'CARS', 'CARE', 'CRI', 'CVNA', 'CASA', 'CWST', 'CASY', 'CSPR', 'CASS', 'SAVA', 'CSTL', 'CSLT', 'CTLT', 'CPRX', 'CTT', 'CAT', 'CATY', 'CATO', 'CVCO', 'CBZ', 'CBOE', 'CBRE', 'CBTX', 'CDK', 'CDW', 'CECE', 'COF', 'CFFN', 'CPRI', 'CSTR', 'CMO', 'CNC', 'CDEV', 'CNP', 'CSR', 'CENTA', 'CENT', 'CPF', 'LEU', 'CENX', 'CNBKA', 'CNTY', 'CCS', 'CERC', 'CRNC', 'CERE', 'CDAY', 'CERN', 'CERT', 'CERS', 'CEVA', 'CF', 'CHX', 'CHNG', 'ECOM', 'CHPT', 'CRL', 'GTLS', 'CHTR', 'CCF', 'CLDT', 'CAKE', 'CHEF', 'CHGG', 'CHE', 'CCXI', 'CC', 'LNG', 'CHK', 'CPK', 'CVX', 'CSSE', 'CHS', 'PLCE', 'CE', 'CELC', 'CLDX', 'CVM', 'CELH', 'CB', 'CHD', 'CHDN', 'CHUY', 'CIEN', 'CI', 'XEC', 'CMPR', 'CBB', 'CINF', 'CNK', 'CTAS', 'CIR', 'CRUS', 'CSCO', 'CIT', 'CTRN', 'C', 'CTXR', 'CZNC', 'CFG', 'CIA', 'CTXS', 'CHCO', 'CIO', 'CIVB', 'CLVT', 'CLAR', 'CLNE', 'CLH', 'CLSK', 'CCO', 'CLFD', 'CLPT', 'CLW', 'CWEN.A', 'CWEN', 'CLNN', 'CLF', 'CLPR', 'CLX', 'CLDR', 'NET', 'CIM', 'CMRX', 'KDNY', 'CMG', 'CHH', 'CDXC', 'CNO', 'CNX', 'CCB', 'KO', 'COKE', 'CDXS', 'CDAK', 'CDE', 'COGT', 'CCOI', 'CGNX', 'CTSH', 'CNS', 'COHR', 'CHRS', 'COHU', 'CFX', 'CL', 'COLL', 'COLB', 'CLBK', 'CXP', 'COLM', 'CMCO', 'CMCSA', 'CMA', 'FIX', 'CBSH', 'CMC', 'CVGI', 'COMM', 'CBU', 'CYH', 'CHCT', 'CTBI', 'CVLT', 'CMP', 'CPSI', 'CIX', 'SCOR', 'CRK', 'CMTL', 'CLVS', 'CCMP', 'CME', 'CMS', 'CNA', 'CCNE', 'COP', 'ED', 'CEIX', 'CNSL', 'STZ', 'CNST', 'CSTM', 'ROAD', 'MCF', 'CLR', 'COO', 'CPS', 'CPA', 'CPRT', 'CORT', 'CXW', 'CORE', 'CPLG', 'COR', 'CRMD', 'CNR', 'CSOD', 'GLW', 'OFC', 'CRSR', 'CTVA', 'CRTX', 'CRVL', 'CMRE', 'CSGP', 'COST', 'COTY', 'COUP', 'COUR', 'CUZ', 'CVA', 'CVLG', 'CVET', 'COWN', 'CRAI', 'CBRL', 'CR', 'CAG', 'CNXC', 'BBCP', 'CNDT', 'CNMD', 'CNOB', 'CONN', 'CRWD', 'CCI', 'CCK', 'CRY', 'CYRX', 'CSGS', 'CSWI', 'CSX', 'CTO', 'CTS', 'CUBE', 'CUE', 'CFR', 'CGEM', 'CMI', 'CVAC', 'CURI', 'CRIS', 'CURO', 'CW', 'CWK', 'CTOS', 'CUBI', 'CUTR', 'CVBF', 'CVI', 'CVS', 'CBAY', 'CONE', 'CYTK', 'CTMX', 'CTSO', 'DHI', 'DJCO', 'DAKT', 'DAN', 'DHR', 'DNMR', 'DRI', 'DRIO', 'DAR', 'CRD.A', 'CACC', 'CREE', 'CRNX', 'CROX', 'CCRN', 'CFB', 'TACO', 'DK', 'DELL', 'DAL', 'DLX', 'DNLI', 'DEN', 'DENN', 'XRAY', 'DMTK', 'DSGN', 'DBI', 'DM', 'DVN', 'DXCM', 'DHT', 'DHIL', 'DSSI', 'FANG', 'DRH', 'DRNA', 'DKS', 'DBD', 'DGII', 'DMRC', 'DMS', 'DLR', 'APPS', 'DBRG', 'DOCN', 'DDS', 'DCOM', 'DIN', 'DIOD', 'DFS', 'DISCA', 'DISCK', 'DISH', 'DIS', 'DSEY', 'DHC', 'DSKE', 'DDOG', 'MSP', 'PLAY', 'DVA', 'DCPH', 'DECK', 'DE', 'UFS', 'DCI', 'DGICA', 'RRD', 'DFIN', 'DASH', 'LPG', 'DORM', 'DV', 'PLOW', 'DEI', 'DOV', 'DOW', 'DKNG', 'DRQ', 'DS', 'DRVN', 'DBX', 'DSPG', 'DTE', 'DCT', 'NAPA', 'DCO', 'DUK', 'DRE', 'DLTH', 'DNB', 'DD', 'DRRX', 'DXC', 'DXPE', 'DY', 'DT', 'DVAX', 'DYN', 'DX', 'DZSI', 'ELF', 'ETWO', 'EGBN', 'BOOM', 'DOCU', 'DLB', 'DG', 'DLTR', 'D', 'DPZ', 'DOMO', 'EMN', 'KODK', 'ETN', 'EBAY', 'EBIX', 'ECHO', 'SATS', 'ECL', 'EPC', 'EWTX', 'EIX', 'EDIT', 'EW', 'EGAN', 'EHTH', 'EIGR', 'LOCO', 'ELAN', 'ESTC', 'EA', 'ESI', 'EFC', 'EME', 'EMKR', 'EEX', 'EBS', 'EMR', 'ESRT', 'EIG', 'ENTA', 'EHC', 'ECPG', 'WIRE', 'ENDP', 'ENR', 'UUUU', 'ERII', 'EPAC', 'ENS', 'EBF', 'EGLE', 'EXP', 'EGRX', 'EAR', 'ESTE', 'EWBC', 'DEA', 'EBC', 'EGP', 'EVC', 'ENV', 'NVST', 'EOG', 'EOSE', 'EPAM', 'EPZM', 'PLUS', 'EPR', 'EQT', 'EFX', 'EQIX', 'EQH', 'ETRN', 'EQBK', 'EQC', 'ELS', 'EQR', 'ERIE', 'ESGC', 'ESCA', 'ESE', 'ESPR', 'EBET', 'ESNT', 'EPRT', 'WTRG', 'ESS', 'ETH', 'ETSY', 'EEFT', 'EVLO', 'EB', 'EVBG', 'EVR', 'RE', 'EVRG', 'EVRI', 'EVER', 'ENVA', 'ENPH', 'NPO', 'ENSG', 'ESGR', 'ENTG', 'ETR', 'EBTC', 'EFSC', 'EXC', 'EXLS', 'XONE', 'EXPI', 'EXPE', 'EXPD', 'EXPO', 'EXR', 'XOG', 'EXTR', 'XOM', 'EYPT', 'EZPW', 'FNB', 'FFIV', 'FN', 'FB', 'FDS', 'FICO', 'FLMN', 'FMNB', 'FPI', 'FARO', 'FAST', 'FSLY', 'FATE', 'FTHM', 'FBK', 'AGM', 'FRT', 'FSS', 'FHI', 'FDX', 'FOE', 'FGEN', 'FDBC', 'FIS', 'FRGI', 'FITB', 'ES', 'EVTC', 'EVI', 'EVOP', 'EVH', 'EOLS', 'AQUA', 'EXAS', 'XGN', 'EXEL', 'FCBP', 'FCNCA', 'FCF', 'FCBC', 'FFBC', 'FFIN', 'THFF', 'FFWM', 'FHB', 'FHN', 'FR', 'INBK', 'FIBK', 'FLIC', 'FRME', 'FMBH', 'FMBI', 'FRC', 'FSLR', 'FCFS', 'FE', 'FISV', 'FSR', 'FIVE', 'FSBC', 'FIVN', 'FBC', 'FLT', 'FLXN', 'FLXS', 'FND', 'FLO', 'FLS', 'FLNT', 'FLDM', 'FLR', 'FFIC', 'FMC', 'FOA', 'FISI', 'FNCH', 'FEYE', 'FAF', 'FBNC', 'FBP', 'FBMS', 'FRBA', 'BUSE', 'FRTA', 'FTNT', 'FTV', 'FBIO', 'FBHS', 'FWRD', 'FOSL', 'FCPT', 'FOXA', 'FOX', 'FOXF', 'FRG', 'FC', 'FELE', 'BEN', 'FSP', 'FI', 'FCX', 'FREQ', 'FDP', 'FRPT', 'FTDR', 'ULCC', 'FRO', 'FRPH', 'FSBW', 'FTCI', 'FCN', 'FTSI', 'FUBO', 'FCEL', 'FULC', 'FLGT', 'FLL', 'FUL', 'FULT', 'FNKO', 'FF', 'FNF', 'FOCS', 'FHTX', 'FL', 'F', 'FOR', 'FORA', 'FMTX', 'FORM', 'FORR', 'FBRX', 'GATO', 'GATX', 'GCMG', 'GCP', 'GMTX', 'GNK', 'GNRC', 'GD', 'GE', 'GIS', 'GM', 'GBIO', 'GCO', 'GNUS', 'G', 'GNTX', 'THRM', 'GPC', 'GNW', 'GEO', 'GABC', 'GERN', 'GTY', 'GEVO', 'ROCK', 'GILD', 'GBCI', 'GOOD', 'LAND', 'GLT', 'GKOS', 'GBT', 'GIC', 'GMRE', 'GNL', 'GPN', 'GWRS', 'GTHX', 'GBL', 'GME', 'GLPI', 'GAN', 'GCI', 'GPS', 'GRMN', 'IT', 'GTES', 'GIII', 'GSHD', 'GPRO', 'GRC', 'GOSS', 'GPX', 'GRA', 'GGG', 'EAF', 'GHC', 'GWW', 'LOPE', 'GVA', 'GPMT', 'GPK', 'GTN', 'AJX', 'GLDD', 'GSBC', 'GWB', 'GRBK', 'GDOT', 'GPRE', 'GBOX', 'GBX', 'GHL', 'GNLN', 'GLRE', 'GSKY', 'GLSI', 'GEF', 'GEF.B', 'GDYN', 'GFF', 'GRTS', 'GO', 'GPI', 'GRPN', 'GSAT', 'GLOB', 'GL', 'GMED', 'GDDY', 'GOGO', 'GOCO', 'GLNG', 'GDEN', 'GNOG', 'GS', 'GT', 'HAL', 'HALO', 'HBB', 'HLNE', 'HWC', 'HBI', 'HNGR', 'HAFC', 'HASI', 'THG', 'HONE', 'HOG', 'HLIT', 'HRMY', 'HARP', 'HSC', 'HIG', 'HBIO', 'HAS', 'HVT', 'HE', 'HA', 'HWKN', 'HAYN', 'HAYW', 'HBT', 'HCHC', 'HCA', 'HCI', 'HCAT', 'HR', 'HCSG', 'HTA', 'HQY', 'PEAK', 'HSTM', 'GRWG', 'GTBP', 'GTYH', 'GNTY', 'GH', 'GES', 'GWRE', 'GMS', 'HEES', 'HAE', 'HAIN', 'HOFV', 'HLF', 'HRI', 'HTBK', 'HCCI', 'HFWA', 'HRTG', 'MLHR', 'HRTX', 'HT', 'HSY', 'HSKA', 'HES', 'HPE', 'HXL', 'HFFG', 'HIBB', 'HPK', 'HIW', 'HI', 'HRC', 'HTH', 'HGV', 'HLT', 'HIFS', 'HQI', 'HNI', 'HFC', 'HOLX', 'HBCP', 'HOMB', 'HD', 'HMPT', 'HMST', 'HTBI', 'FIXX', 'HNST', 'HTLD', 'HTLF', 'HL', 'HEI.A', 'HEI', 'HSII', 'HELE', 'HLIO', 'HLX', 'HP', 'HMTV', 'JKHY', 'HSIC', 'HBMD', 'HHC', 'HWM', 'HPQ', 'HUBG', 'HUBB', 'HUBS', 'HPP', 'HUM', 'HGEN', 'JBHT', 'HBAN', 'HII', 'HUN', 'HURN', 'H', 'HYFM', 'HYLN', 'HYRE', 'HY', 'IIIV', 'IAA', 'IAC', 'IBEX', 'IBIO', 'ICAD', 'ICFI', 'ICHR', 'ICUI', 'IDA', 'IDEX', 'IDYA', 'IEX', 'IDXX', 'IDT', 'HON', 'HOFT', 'HOOK', 'HOPE', 'HMN', 'HBNC', 'HZNP', 'HRL', 'HST', 'TWNK', 'HMHC', 'HLI', 'HOV', 'PI', 'NARI', 'INCY', 'INVE', 'IHC', 'IRT', 'IBCP', 'IBTX', 'INDB', 'INDT', 'ILPT', 'INFN', 'INFI', 'IEA', 'INFU', 'IR', 'NGVT', 'IMKTA', 'INGR', 'INBX', 'IOSP', 'INNV', 'IIPR', 'INVA', 'INGN', 'NOTV', 'INOV', 'INO', 'INZY', 'INSG', 'NSIT', 'INSM', 'NSP', 'INSP', 'IBP', 'IESC', 'IGMS', 'IHRT', 'INFO', 'IIVI', 'IKNA', 'ITW', 'ILMN', 'IMAX', 'IMUX', 'IBRX', 'IMGN', 'IMVT', 'IMPL', 'IBM', 'IGT', 'IMXI', 'IP', 'INSW', 'IPG', 'XENT', 'IBOC', 'IFF', 'ITCI', 'IPI', 'INTU', 'ISRG', 'IVC', 'IVZ', 'IVR', 'ISBC', 'ITIC', 'NVTA', 'INVH', 'IONS', 'IOVA', 'IPGP', 'IQV', 'IRMD', 'IRTC', 'IRDM', 'IRBT', 'IRM', 'IRWD', 'STAR', 'ITOS', 'ITI', 'ITRI', 'IIIN', 'TIL', 'PODD', 'ITGR', 'IART', 'INTC', 'INS', 'NTLA', 'IPAR', 'IBKR', 'ICPT', 'ICE', 'IDCC', 'TILE', 'JBLU', 'FROG', 'JOAN', 'JBT', 'JNJ', 'JCI', 'JOUT', 'JYNT', 'JLL', 'JNCE', 'JPM', 'JNPR', 'KAI', 'KDMN', 'KALU', 'KALA', 'KLDO', 'KALV', 'KAMN', 'KSU', 'KAR', 'KRT', 'KRTX', 'KPTI', 'KBH', 'KBR', 'KRNY', 'K', 'KELYA', 'KMPR', 'KMPH', 'KMT', 'KW', 'KROS', 'ITT', 'ISEE', 'JJSF', 'SJM', 'JCOM', 'JBL', 'JACK', 'J', 'JRVR', 'JAMF', 'JHG', 'JAZZ', 'JBGS', 'JEF', 'JELD', 'KIRK', 'KRG', 'KKR', 'KREF', 'KLAC', 'KNX', 'KNL', 'KN', 'KOD', 'KSS', 'KTB', 'KOPN', 'KOP', 'KFY', 'KOS', 'KHC', 'KRA', 'KTOS', 'KR', 'KRON', 'KRO', 'KRYS', 'KLIC', 'KURA', 'KRUS', 'KVHI', 'KYMR', 'LB', 'LHX', 'LH', 'LADR', 'LSF', 'LBAI', 'KDP', 'KEY', 'KEYS', 'KZR', 'KFRC', 'KRC', 'KE', 'KBAL', 'KMB', 'KIM', 'KMI', 'KNSA', 'KNTE', 'KNSL', 'KEX', 'EL', 'LAUR', 'LAWS', 'LAZ', 'LAZY', 'LCII', 'LEA', 'LEGH', 'LEG', 'LDOS', 'LMAT', 'LMND', 'LC', 'TREE', 'LEN', 'LEN.B', 'LII', 'LESL', 'LXRX', 'LXP', 'LGIH', 'LHCG', 'BATRA', 'BATRK', 'LBRDA', 'LBRDK', 'FWONA', 'FWONK', 'LILA', 'LILAK', 'LBRT', 'LSXMA', 'LSXMK', 'LKFN', 'LRCX', 'LAMR', 'LW', 'LANC', 'LNDC', 'LABP', 'LE', 'LSEA', 'LSTR', 'LNTH', 'LPI', 'LVS', 'SWIM', 'LSCC', 'LZB', 'LFUS', 'LIVN', 'LYV', 'LOB', 'LTHM', 'LPSN', 'RAMP', 'LIVX', 'LKQ', 'LMT', 'L', 'LORL', 'RIDE', 'LPX', 'LOVE', 'LOW', 'LPLA', 'LTC', 'LULU', 'LL', 'LUMN', 'LITE', 'LMNX', 'LUNA', 'LBC', 'LXFR', 'LDL', 'LYFT', 'LYB', 'MTB', 'MHO', 'MCBC', 'LTRPA', 'LSI', 'LCUT', 'LGND', 'LLY', 'LLNW', 'LMNR', 'LECO', 'LNC', 'LIND', 'LNN', 'LCTX', 'LGF.A', 'LGF.B', 'LQDT', 'LAD', 'MNKD', 'MAN', 'MANT', 'MARA', 'MRO', 'MPC', 'MRVI', 'MMI', 'MCS', 'MPX', 'HZO', 'MRNS', 'MKL', 'MKTX', 'MRLN', 'MAR', 'VAC', 'MBII', 'MMC', 'MRTN', 'MLM', 'MRVL', 'MAS', 'MASI', 'DOOR', 'MTZ', 'MA', 'MCFT', 'MTDR', 'MTCH', 'MTRN', 'MTRX', 'MAC', 'CLI', 'MTSI', 'MIC', 'MGNX', 'M', 'MSGE', 'MSGS', 'MDGL', 'MGLN', 'MGTA', 'MGNI', 'MGY', 'MHLD', 'MBUU', 'MANH', 'MTW', 'MDLA', 'MDVL', 'MAX', 'MPW', 'MED', 'MD', 'MEDP', 'MDT', 'MEIP', 'MGTX', 'MBWM', 'MBIN', 'MRK', 'MCY', 'MRCY', 'MDP', 'EBSB', 'VIVO', 'MMSI', 'MTH', 'MTOR', 'MRSN', 'MESA', 'MLAB', 'CASH', 'MEI', 'MET', 'MCBS', 'MILE', 'MCB', 'MTD', 'MATX', 'MAT', 'MATW', 'MAXR', 'MXIM', 'MMS', 'MXL', 'MEC', 'MBI', 'MCFE', 'MKC', 'MCD', 'MGRC', 'MCK', 'MDC', 'MDCA', 'MDU', 'MDXG', 'MNMD', 'MTX', 'MRTX', 'MIRM', 'MSON', 'AVO', 'MG', 'MITK', 'MKSI', 'MODN', 'MRNA', 'MOD', 'MODV', 'MC', 'MHK', 'MTEM', 'MOH', 'TAP', 'MNTV', 'MCRI', 'MDLZ', 'MGI', 'MDB', 'MNR', 'MPWR', 'MNRO', 'MNST', 'MEG', 'MCO', 'MOG.A', 'MFA', 'MGEE', 'MTG', 'MGM', 'MGPI', 'MCHP', 'MU', 'MSFT', 'MSTR', 'MVIS', 'MPB', 'MAA', 'MIDD', 'MSEX', 'MSBI', 'MOFG', 'MLR', 'MIME', 'MUSA', 'MBIO', 'MVBF', 'MYE', 'MYRG', 'MYGN', 'NBR', 'NSTG', 'NH', 'NSSC', 'NDAQ', 'NTRA', 'NATH', 'NBHC', 'FIZZ', 'NCMI', 'NESR', 'NHI', 'NHC', 'NATI', 'NPK', 'NRC', 'NNN', 'NSA', 'EYE', 'NWLI', 'NFG', 'NGVC', 'NATR', 'NTUS', 'MS', 'MORN', 'MORF', 'MOS', 'MPAA', 'MSI', 'MOV', 'MP', 'COOP', 'MRC', 'MSA', 'MSM', 'MSCI', 'MSGN', 'MLI', 'MWA', 'MPLN', 'MUR', 'NBIX', 'STIM', 'NPCE', 'NVRO', 'NFE', 'NJR', 'NEWR', 'NRZ', 'SNR', 'NYCB', 'NYMT', 'NYT', 'NBEV', 'NWL', 'NMRK', 'NEU', 'NEM', 'NR', 'NWSA', 'NWS', 'NEXI', 'NXRT', 'NXST', 'NEE', 'NXGN', 'NEX', 'NGM', 'NODK', 'NCBS', 'NLSN', 'NLS', 'NAVI', 'NAV', 'NBTB', 'NCNO', 'NCR', 'NP', 'NKTR', 'NNI', 'NGMS', 'NEOG', 'NEO', 'NLTX', 'NPTN', 'NTAP', 'NFLX', 'NTGR', 'NTCT', 'NTST', 'NWN', 'NWPX', 'NWE', 'NLOK', 'NCLH', 'NOV', 'NG', 'NOVT', 'NVAX', 'NVCR', 'DNOW', 'NRG', 'NUS', 'NUAN', 'NUE', 'NRIX', 'NTNX', 'NUVA', 'NUVB', 'NVEE', 'NVEC', 'NVT', 'NVDA', 'NVR', 'NXPI', 'ORLY', 'OSH', 'OAS', 'OXY', 'NKE', 'NKLA', 'NI', 'NKTX', 'NL', 'LASR', 'NMIH', 'NNBR', 'NDLS', 'NAT', 'NDSN', 'JWN', 'NSC', 'NOG', 'NTRS', 'NFBK', 'NRIM', 'NOC', 'NWBI', 'OFLX', 'OHI', 'OMER', 'OMCL', 'OMC', 'ON', 'ONTF', 'OCX', 'ONCR', 'ONCT', 'OGS', 'STKS', 'OLP', 'OMF', 'OKE', 'OSPN', 'OSW', 'ONEW', 'ONTO', 'OTRK', 'OOMA', 'LPRO', 'OPEN', 'OPK', 'OPRT', 'OPY', 'OPRX', 'OPCH', 'ORCL', 'OII', 'OCFC', 'OCGN', 'OCUL', 'OCN', 'OPI', 'OFG', 'OGE', 'OI', 'ODC', 'OIS', 'OKTA', 'ODFL', 'ONB', 'ORI', 'OSBC', 'OLMA', 'OLN', 'OLLI', 'ZEUS', 'OTLK', 'OM', 'OSTK', 'OVV', 'OMI', 'OC', 'OXM', 'OYST', 'PTSI', 'PCAR', 'PACB', 'PPBI', 'PCRX', 'PKG', 'PTVE', 'PACW', 'PAE', 'PD', 'PLTR', 'PANW', 'PLMR', 'PZZA', 'PARR', 'PAR', 'PGRE', 'PRTK', 'PKE', 'PK', 'ORMP', 'OSUR', 'ORBC', 'ORC', 'ORGO', 'OGN', 'ORIC', 'OBNK', 'OEC', 'ORA', 'ORRF', 'OCDX', 'OFIX', 'KIDS', 'OSK', 'OSIS', 'OTIS', 'OTTR', 'OUST', 'OUT', 'BTU', 'PGC', 'PEB', 'PEGA', 'PTON', 'PENN', 'PVAC', 'PNTG', 'PFSI', 'PMT', 'PAG', 'PNR', 'PEN', 'PEBO', 'PFIS', 'PBCT', 'PEP', 'PRDO', 'PRFT', 'PFGC', 'PKI', 'PPTA', 'PRGO', 'PSNL', 'WOOF', 'PETQ', 'PETS', 'PFE', 'PRK', 'PKOH', 'PH', 'PSN', 'PRTY', 'PASG', 'PATK', 'PDCO', 'PTEN', 'PAVM', 'PAYA', 'PAYX', 'PAYC', 'PCTY', 'PYPL', 'PSFE', 'PBF', 'CNXN', 'PCSB', 'PDCE', 'PDFS', 'POLY', 'AGS', 'PLTK', 'PLBY', 'PLXS', 'PLRX', 'PLUG', 'PLYM', 'PMVP', 'PNC', 'PNM', 'PII', 'PLM', 'POOL', 'BPOP', 'PRCH', 'PRTG', 'POR', 'PSTX', 'POST', 'PSTL', 'PCH', 'POWL', 'POWI', 'PPD', 'PPG', 'PPL', 'PCG', 'PGTI', 'PHAT', 'PAHC', 'PM', 'PSX', 'PLAB', 'PHR', 'DOC', 'PDM', 'PPC', 'PING', 'PNFP', 'PNW', 'PINS', 'PBFS', 'PXD', 'PIPR', 'PBI', 'PJT', 'PLNT', 'PRVA', 'PRA', 'PG', 'PRG', 'PRGS', 'PGR', 'PGNY', 'PLD', 'RXDX', 'PFPT', 'PUMP', 'PRO', 'PROS', 'PB', 'PTGX', 'PRTA', 'PRLB', 'PRVB', 'PVBC', 'PFS', 'PRU', 'PSB', 'PTC', 'PTCT', 'PSA', 'PEG', 'LUNG', 'PQG', 'PRAA', 'PRAH', 'PRAX', 'PGEN', 'DTIL', 'APTS', 'PFBC', 'PLPC', 'PRLD', 'PFC', 'PFBI', 'PINC', 'PBH', 'TROW', 'PSMT', 'PRI', 'FRST', 'PRMW', 'PRIM', 'PFG', 'PRTH', 'QS', 'DGX', 'QDEL', 'QNST', 'QTNT', 'QUOT', 'QRTEA', 'RXT', 'RDN', 'RLGT', 'RADI', 'RDUS', 'RDNT', 'RFL', 'RAIN', 'RL', 'RMBS', 'RRC', 'PACK', 'RPD', 'RAPT', 'RAVN', 'RJF', 'RYN', 'RYAM', 'RTX', 'PLSE', 'PHM', 'PBYI', 'PSTG', 'PCYO', 'PCT', 'PRPL', 'PVH', 'PZN', 'QTWO', 'QADA', 'QCRH', 'QGEN', 'QRVO', 'QTS', 'KWR', 'QCOM', 'QLYS', 'NX', 'PWR', 'QTRX', 'QMCO', 'RLAY', 'RS', 'RBNC', 'RLMD', 'RNR', 'RNST', 'RPHM', 'REGI', 'RCII', 'FRBK', 'RPAY', 'RGEN', 'REPL', 'RBCAA', 'RSG', 'REZI', 'RMD', 'RGP', 'ROIC', 'RPAI', 'RVI', 'RVP', 'REVG', 'RVNC', 'REV', 'RVMD', 'RBB', 'ROLL', 'RICK', 'RMAX', 'RC', 'RLGY', 'O', 'RETA', 'RXRX', 'RRBI', 'RRGB', 'RRR', 'RDFN', 'RWT', 'RBC', 'REG', 'REGN', 'RGNX', 'RM', 'RF', 'RGS', 'RGA', 'REKR', 'ROKU', 'ROL', 'RMO', 'ROP', 'ROST', 'RCL', 'RGLD', 'RPRX', 'RES', 'RPM', 'RPT', 'RUBY', 'RUSHA', 'RUSHB', 'RSI', 'RUTH', 'R', 'RYI', 'RHP', 'SPGI', 'STBA', 'SBRA', 'SABR', 'SB', 'SAFE', 'RVLV', 'REX', 'REXR', 'RXN', 'REYN', 'RH', 'RYTM', 'RBBN', 'RIGL', 'REPX', 'RMNI', 'RNG', 'RIOT', 'RAD', 'RLI', 'RLJ', 'RMR', 'RHI', 'RKT', 'RCKT', 'ROK', 'RCKY', 'ROG', 'SCHW', 'SWM', 'SAIC', 'SGMS', 'STNG', 'SMG', 'SSP', 'SCU', 'SEB', 'SBCF', 'SGEN', 'SEE', 'SPNE', 'SEAS', 'SCWX', 'SEEL', 'SEER', 'SEIC', 'WTTR', 'SEM', 'SELB', 'SIGI', 'SLQT', 'SRE', 'SMTC', 'SAFT', 'SAGE', 'SAIA', 'SAIL', 'CRM', 'SBH', 'SANA', 'SAFM', 'SASR', 'JBSS', 'SGMO', 'SANM', 'SC', 'SPNS', 'SRPT', 'BFS', 'SBAC', 'SCSC', 'SLB', 'SNDR', 'SCHN', 'SRRK', 'SCHL', 'SDGR', 'SSTK', 'SIBN', 'SIEN', 'BSRR', 'SIGA', 'SGTX', 'SBNY', 'SIG', 'SGFY', 'SLGN', 'SLAB', 'SILK', 'SBTX', 'SI', 'SFNC', 'SPG', 'SMPL', 'SSD', 'SLP', 'SBGI', 'SIRI', 'SPNT', 'SITC', 'SITE', 'SENEA', 'ST', 'SNSE', 'SENS', 'SXT', 'MCRB', 'SRG', 'SCI', 'SVC', 'NOW', 'SFBS', 'SESN', 'SFL', 'SHAK', 'SMED', 'STTK', 'SHEN', 'SHW', 'SFT', 'FOUR', 'SHLS', 'SWAV', 'SCVL', 'SSTI', 'SLDB', 'SOLY', 'SAH', 'SON', 'SONO', 'SRNE', 'SHC', 'SJI', 'SPFI', 'SSB', 'SO', 'SCCO', 'SFST', 'SBSI', 'LUV', 'SWX', 'SWN', 'SP', 'SPKE', 'SPTN', 'SPB', 'SPPI', 'SPRO', 'SR', 'SITM', 'SIX', 'SJW', 'SKX', 'SKLZ', 'SKY', 'SKYT', 'SKYW', 'SWKS', 'SLG', 'WORK', 'SNBR', 'SLM', 'SM', 'SGH', 'SMBK', 'SMAR', 'AOS', 'SWBI', 'SMSI', 'SNA', 'SNOW', 'TLMD', 'SOI', 'SWI', 'STWD', 'STFC', 'STT', 'SMP', 'STLD', 'SCS', 'STEM', 'SCL', 'STEP', 'STXS', 'SRCL', 'STE', 'STL', 'STRL', 'SHOO', 'STC', 'SMBC', 'SF', 'SFIX', 'SYBT', 'STOK', 'STNE', 'STON', 'SPR', 'SAVE', 'STXB', 'SRC', 'SPLK', 'SPWH', 'SPOT', 'SWTX', 'SPT', 'SFM', 'SPRB', 'SPSC', 'SPXC', 'FLOW', 'SQ', 'SQZ', 'SSNC', 'JOE', 'STAA', 'STAG', 'STMP', 'SXI', 'SWK', 'SBUX', 'SRT', 'SIVB', 'SWCH', 'SYKE', 'SYNA', 'SYF', 'SNDX', 'SYNH', 'SNX', 'SNPS', 'SNV', 'SYRS', 'SYY', 'TRHC', 'TCMD', 'TTWO', 'TALS', 'TLIS', 'TALO', 'TNDM', 'SKT', 'TPR', 'TRGP', 'TGT', 'SRI', 'SNEX', 'STOR', 'STRA', 'LRN', 'SYK', 'RGR', 'SMMF', 'INN', 'SUM', 'SMMT', 'SUMO', 'SUI', 'SNCY', 'SXC', 'NOVA', 'SPWR', 'RUN', 'SHO', 'SMCI', 'SGC', 'SUPN', 'SURF', 'SGRY', 'SRDX', 'STRO', 'TEX', 'TMX', 'TERN', 'TRNO', 'TSLA', 'TTEK', 'TTI', 'TCBI', 'TXN', 'TPL', 'TXRH', 'TGH', 'TXT', 'TFSL', 'TGTX', 'AAN', 'AZEK', 'TBBK', 'BX', 'TCS', 'FNLC', 'HCKT', 'TH', 'TARS', 'TTCF', 'TMHC', 'TSHA', 'TCRR', 'TISI', 'TTGT', 'TK', 'TNK', 'TGNA', 'TRC', 'TDOC', 'TDY', 'TFX', 'TDS', 'TELL', 'TLS', 'TPX', 'TENB', 'THC', 'TNC', 'TEN', 'TDC', 'TER', 'TMUS', 'TRTX', 'TPIC', 'TSCO', 'TW', 'TT', 'TRNS', 'TDG', 'TBIO', 'TMDX', 'TRU', 'TNL', 'TA', 'TRV', 'TVTX', 'TMCI', 'TIG', 'TG', 'THS', 'TRVN', 'TREX', 'TPH', 'TCBK', 'ODP', 'REAL', 'SHYF', 'TTD', 'TXMD', 'TBPH', 'TMO', 'THR', 'THO', 'THRY', 'TDW', 'TLYS', 'TKR', 'TMST', 'TIPT', 'TWI', 'TITN', 'TVTY', 'TJX', 'TOL', 'TMP', 'TNXP', 'TR', 'BLD', 'TRCH', 'TTC', 'TOWN', 'TPC', 'TWLO', 'TWST', 'TWTR', 'TWO', 'TYL', 'TSN', 'USM', 'USLM', 'USX', 'UBER', 'UI', 'UDR', 'UFPI', 'UFPT', 'UGI', 'ULTA', 'UCTT', 'RARE', 'UMBF', 'UMH', 'TRIL', 'TRS', 'TRMB', 'TNET', 'TRN', 'TSE', 'TRIP', 'GTS', 'TSC', 'TRTN', 'TBK', 'TGI', 'TROX', 'TBI', 'TRUE', 'TFC', 'TRUP', 'TRST', 'TRMK', 'TTEC', 'TTMI', 'TCX', 'TUP', 'TPB', 'TPTX', 'HEAR', 'TSP', 'UVSP', 'UNM', 'UPLD', 'UPST', 'UPWK', 'UEC', 'UE', 'URBN', 'URG', 'URGN', 'UBA', 'USB', 'USCR', 'ECOL', 'USFD', 'USPH', 'SLCA', 'USNA', 'UTMD', 'UBSI', 'UTZ', 'UMPQ', 'UAA', 'UA', 'UFI', 'UNF', 'UNP', 'UIS', 'UAL', 'UCBI', 'UFCS', 'UIHC', 'UNFI', 'UPS', 'URI', 'X', 'UTHR', 'UNH', 'UNIT', 'UTL', 'U', 'UNVR', 'UVV', 'OLED', 'UEIC', 'UHT', 'UHS', 'UVE', 'ULH', 'VRSN', 'VRSK', 'VBTX', 'VRTV', 'VERI', 'VZ', 'VRRM', 'VRCA', 'VRS', 'VRTX', 'VRT', 'VERU', 'VFC', 'VIACA', 'VIAC', 'VVI', 'DSP', 'VSAT', 'VTRS', 'VIAV', 'UWMC', 'MTN', 'VLO', 'VHI', 'VLY', 'VMI', 'VALU', 'VVV', 'VNDA', 'VAPO', 'VREX', 'VRNS', 'VXRT', 'PCVX', 'VBIV', 'VGR', 'VEC', 'VECO', 'VEEV', 'VEL', 'VLDR', 'VTR', 'VRA', 'VCYT', 'VSTM', 'VER', 'VCEL', 'VRNT', 'VOR', 'VNO', 'VOXX', 'VOYA', 'VRM', 'VSEC', 'VMC', 'VUZI', 'WTI', 'WPC', 'WNC', 'WAB', 'WBA', 'WD', 'WMT', 'HCC', 'WAFD', 'WRE', 'WASH', 'WM', 'VICI', 'VICR', 'VMD', 'VIEW', 'VRAY', 'VKTX', 'VLGEA', 'VMEO', 'VINC', 'VEI', 'VIR', 'VIRX', 'SPCE', 'VHC', 'VIRT', 'VRTS', 'V', 'VSH', 'VPG', 'VSTO', 'VTGN', 'VC', 'VST', 'VITL', 'VVNT', 'VMW', 'VCRA', 'VG', 'VNT', 'WY', 'WHR', 'WTM', 'WSR', 'WLL', 'FREE', 'WOW', 'JW.A', 'WLDN', 'WMB', 'WSM', 'WLFC', 'WLTW', 'WSC', 'WING', 'WINA', 'WGO', 'WTFC', 'WETF', 'WAT', 'WSBF', 'WTRE', 'WSO', 'WTS', 'WVE', 'W', 'WDFC', 'WBS', 'WEC', 'WRI', 'WMK', 'WBT', 'WFC', 'WELL', 'WEN', 'HOWL', 'WERN', 'WSBC', 'WCC', 'WTBA', 'WST', 'WABC', 'WAL', 'WDC', 'WU', 'WLK', 'WRK', 'WEX', 'YEXT', 'YORW', 'YUM', 'YUMC', 'ZBRA', 'ZEN', 'ZNTL', 'ZG', 'Z', 'ZBH', 'ZION', 'ZIOP', 'ZIXI', 'ZTS', 'ZGNX', 'ZM', 'ZS', 'ZUMZ', 'ZUO', 'WIX', 'WWW', 'WWD', 'WDAY', 'WKHS', 'WK', 'WRLD', 'INT', 'WOR', 'WSFS', 'WW', 'WWE', 'WH', 'WYNN', 'XBIT', 'XEL', 'XNCR', 'XHR', 'XRX', 'XLNX', 'XL', 'XOMA', 'XPEL', 'XPER', 'XPO', 'XYL', 'YELL', 'YELP', 'YETI', 'YMAB', 'ZY', 'ZYXI', 'ZNGA']

small_cap_list = []
mid_cap_list = []
large_cap_list = []

small_cap_max = 2000000000
mid_cap_max = 10000000000

for stock in russell3000:
    stock_data = yf.Ticker(stock).info
    if stock_data['marketCap'] < small_cap_max:
        small_cap_list.append(stock)
    elif stock_data['marketCap'] <= mid_cap_max:
        mid_cap_list.append(stock)
    else:
        large_cap_list.append(stock)

