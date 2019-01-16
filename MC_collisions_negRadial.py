import FWCore.ParameterSet.Config as cms

process = cms.Process("ReRec")

process.load("CondCore.CondDB.CondDB_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
# pointing skim
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/D4CEBE13-DF66-E811-B9F2-FA163E4BCA1A.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/1EA773E6-E966-E811-B2A5-FA163EF33A09.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/8839C575-0767-E811-BF3E-FA163E79C5A3.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/CCDEA233-0F67-E811-8CB9-FA163E382F9A.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/E0527E60-E366-E811-A413-FA163E3D3BDB.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/883B1449-E366-E811-AF3D-FA163EFE5BB8.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/EE1596CF-2167-E811-94D0-FA163EF2930D.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/D2650F98-ED66-E811-9B73-FA163E9DDD75.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/766F6F43-E466-E811-9BD6-FA163E14F4F9.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/1ECBF0E6-2967-E811-A6ED-FA163E014692.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/E417CFD7-ED66-E811-BA0D-FA163E646D28.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/9C63FF07-FD66-E811-9B97-FA163E7A3462.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/460A5FE5-F666-E811-B52A-FA163EA5274A.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/4824392D-4567-E811-A221-FA163E4171E0.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/BC237E67-2A67-E811-BCC5-FA163E946399.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/862FD602-FD66-E811-AA02-FA163E3B3CCD.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/68A8E987-2767-E811-A7AC-FA163EA5D5A9.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/3CDCC40F-6267-E811-9451-FA163E0838A3.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/2A22E41C-7567-E811-B741-FA163E034AC1.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/143C48E6-2A67-E811-98E7-FA163EB0C6EB.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/A06F2E0A-4867-E811-9D0B-FA163EAFB5E2.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/B02DEFF2-2A67-E811-A386-FA163E7494EC.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/824CE3EF-2A67-E811-B037-FA163E12D4CD.root",
"/store/mc/RunIISpring18DRPremix/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/ALCARECO/TkAlMinBias-TkAlMinBias_100X_upgrade2018_realistic_v10-v1/70000/A6165DD7-1267-E811-80BA-FA163EFE26E6.root",
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
process.GlobalTag.globaltag = '100X_upgrade2018_design_IdealBS_v8'
#process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string('TrackerAlignmentRcd'),
             tag = cms.string('Alignments'),
             connect = cms.string('sqlite_file:/afs/cern.ch/user/j/jfeingol/commonValidation/jfeingold/weakModes/CMSSW_10_1_7/Alignment/TrackerAlignment/test/MC_negRadial.db')
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
    fileName = cms.string('MC_collisions_negRadial.root')
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

