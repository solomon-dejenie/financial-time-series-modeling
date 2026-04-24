
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def run_pca(X,n_components=2):
    Xs=StandardScaler().fit_transform(X)
    pca=PCA(n_components=n_components)
    comps=pca.fit_transform(Xs)
    return comps,pca
