import FWCore.ParameterSet.Config as cms

process = cms.Process("ReRec")

process.load("CondCore.CondDB.CondDB_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
# pointing skim
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/823/00000/782D719C-868B-E811-9E65-02163E017F44.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/822/00000/6E22184C-818B-E811-8625-FA163E5FB578.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/818/00000/429F294F-858B-E811-A459-FA163E7121A5.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/816/00000/EA4DACE7-818B-E811-ACE0-FA163E0E0120.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/815/00000/D08B19B0-828B-E811-A731-FA163E2B0F48.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/814/00000/A6FD2A8D-838B-E811-95D0-FA163EABDB9A.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/813/00000/3A44451B-838B-E811-828E-02163E019F53.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/812/00000/0401E768-858B-E811-B7DC-FA163E629498.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/811/00000/02380996-838B-E811-B991-02163E01A0C9.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/809/00000/BE37D1FA-818B-E811-A02D-FA163E2DDF84.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/800/00000/D2C0E00D-818B-E811-923D-FA163E6CD0D3.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/798/00000/F419CA06-838B-E811-A107-FA163E4A4920.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/794/00000/6A587364-818B-E811-94B9-FA163E45DA89.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/790/00000/9EDB1D40-858B-E811-87B6-FA163E74255C.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/787/00000/0AD6F8F6-828B-E811-94A4-FA163E8F2C56.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/783/00000/7419F259-838B-E811-B7B5-FA163E1E6FE0.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/777/00000/78C4D44D-858B-E811-9A9B-FA163E3F6AE6.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/772/00000/72C959F5-818B-E811-9916-02163E01306C.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/770/00000/2A09FA5B-838B-E811-BC93-FA163EEF5766.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/769/00000/A8905414-7F8B-E811-9B47-FA163E06D5D5.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/768/00000/4E5054DB-7F8B-E811-A364-FA163E3AF57F.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/766/00000/0E281499-7E8B-E811-940A-FA163E7B3AB6.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/765/00000/9A7160FA-828B-E811-AFA6-FA163EB7D818.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/763/00000/689DFF7A-828B-E811-BC79-FA163E946DF0.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/761/00000/E6C5DB26-818B-E811-8E17-FA163EC391A6.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/760/00000/24C4E1C8-7E8B-E811-BEE2-FA163E1499C9.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/759/00000/D2CF37C0-818B-E811-B11A-FA163ED91314.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/758/00000/E44FC137-858B-E811-B233-FA163E139AC8.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/756/00000/F6BA4446-678B-E811-B6EF-02163E01A106.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/756/00000/ECD9CB8A-638B-E811-99B0-FA163EC01FA2.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/756/00000/E65C902B-868B-E811-9EEA-FA163EDC9ED5.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/756/00000/DA76403F-738B-E811-9734-FA163E692103.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/756/00000/D8EFCBAC-768B-E811-9E82-FA163E038E39.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/756/00000/BEAD74D6-7D8B-E811-9A9A-FA163EA79D8C.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/756/00000/BE698621-658B-E811-A16E-FA163ED0971C.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/756/00000/AA407AF7-6E8B-E811-A21B-FA163EBF29F0.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/756/00000/A8E706BF-758B-E811-826B-FA163E55CE78.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/756/00000/A8776FC1-7A8B-E811-8434-FA163E59AE30.root",
"/store/data/Run2018C/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v2/000/319/756/00000/A06E5279-788B-E811-861A-FA163E11DF90.root",
    )
)

# output module#
#process.load("Configuration.EventContent.EventContentCosmics_cff")
#process.load("CalibTracker.SiStripESProducers.SiStripQualityESProducer_cfi")
#process.load("RecoLocalTracker.Configuration.RecoLocalTracker_Cosmics_cff")

#process.load("RecoTracker.MeasurementDet.MeasurementTrackerESProducer_cfi")

# Conditions (Global Tag is used here):
#process.load("Configuration.Geometry.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = '102X_dataRun2_TkAlSummerCamp_SG_v4'
#process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string('TrackerAlignmentRcd'),
             tag = cms.string('Alignments'),
             connect = cms.string('sqlite_file:/afs/cern.ch/user/j/jfeingol/commonValidation/jfeingold/weakModes/CMSSW_10_1_7/Alignment/TrackerAlignment/test/Data_posRadial_BPIX.db'),
    ),
    cms.PSet(record = cms.string('SiPixelTemplateDBObjectRcd'),
             tag = cms.string('SiPixelTemplateDBObject_38T_TempForAlignmentReReco2018_v3'),
             connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    ),
)


#Geometry
#process.load("Configuration.StandardSequences.Geometry_cff")

# Real data raw to digi
#process.load("Configuration.StandardSequences.RawToDigi_Data_cff")

# reconstruction sequence for Cosmics
#process.load("Configuration.StandardSequences.ReconstructionCosmics_cff")

# offline DQM
#process.load("DQMOffline.Configuration.DQMOfflineCosmics_cff")
#process.load("DQMServices.Components.MEtoEDMConverter_cff")

#L1 trigger validation
#process.load("L1Trigger.HardwareValidation.L1HardwareValidation_cff")
#process.load("L1Trigger.Configuration.L1Config_cff")
#process.load("L1TriggerConfig.CSCTFConfigProducers.CSCTFConfigProducer_cfi")
#process.load("L1TriggerConfig.CSCTFConfigProducers.L1MuCSCTFConfigurationRcdSrc_cfi")

#process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.Geometry.GeometryDB_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")


import Alignment.CommonAlignment.tools.trackselectionRefitting as trackselRefit
process.seqTrackselRefit = trackselRefit.getSequence(process, 'ALCARECOTkAlMinBias',
                                                     isPVValidation=False,
                                                     TTRHBuilder='WithAngleAndTemplate',
                                                     usePixelQualityFlag=True,
                                                     openMassWindow=False,
                                                     cosmicsDecoMode=False,
                                                     cosmicsZeroTesla=False,
                                                     momentumConstraint=None,
                                                     cosmicTrackSplitting=False,
                                                     use_d0cut=False,
                                                    )





process.TFileService = cms.Service("TFileService",
    fileName = cms.string('Data_collisions_posRadial_BPIX.root')
)

process.analysis = cms.EDAnalyzer("HitRes",
    usePXB = cms.bool(True),
    usePXF = cms.bool(True),
    useTIB = cms.bool(True),
    useTOB = cms.bool(True),
    useTID = cms.bool(True),
    useTEC = cms.bool(True),
    ROUList = cms.vstring('TrackerHitsTIBLowTof', 
        'TrackerHitsTIBHighTof', 
        'TrackerHitsTOBLowTof', 
        'TrackerHitsTOBHighTof'),
    trajectories = cms.InputTag("FinalTrackRefitter"),
    associatePixel = cms.bool(False),
    associateStrip = cms.bool(False),
    associateRecoTracks = cms.bool(False),
    tracks = cms.InputTag("FinalTrackRefitter"),
    barrelOnly = cms.bool(False)
)

# Path and EndPath definitions
process.p = cms.Path(process.seqTrackselRefit*process.analysis)
#process.endjob_step = cms.Path(process.endOfProcess)

# Schedule definition
#process.schedule = cms.Schedule(process.p,process.endjob_step)
process.schedule = cms.Schedule(process.p)

