from model.bsarec import BSARecModel
from model.caser import CaserModel
from model.gru4rec import GRU4RecModel
from model.sasrec import SASRecModel
from model.bert4rec import BERT4RecModel
from model.fmlprec import FMLPRecModel
from model.duorec import DuoRecModel
from model.fearec import FEARecModel
from model.bsarec_s_a import BSARecModel_S_A
from model.bsarec_sa_s import BSARecModel_SA_S
from model.bsarec_sa_a import BSARecModel_SA_A
from model.bsarec_sa_s_a import BSARecModel_SA_S_A
from model.bsarec_s import BSARecModel_S
from model.bsarec_a import BSARecModel_A

MODEL_DICT = {
    "bsarec_a": BSARecModel_A,
    "bsarec_s": BSARecModel_S,
    "bsarec_sa_s_a": BSARecModel_SA_S_A,
    "bsarec_sa_a": BSARecModel_SA_A,
    "bsarec_sa_s": BSARecModel_SA_S,
    "bsarec_s_a": BSARecModel_S_A,
    "bsarec": BSARecModel,
    "caser": CaserModel,
    "gru4rec": GRU4RecModel,
    "sasrec": SASRecModel,
    "bert4rec": BERT4RecModel,
    "fmlprec": FMLPRecModel,
    "duorec": DuoRecModel,
    "fearec": FEARecModel,
    }