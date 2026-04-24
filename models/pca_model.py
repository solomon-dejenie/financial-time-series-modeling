
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def run_pca(X, n=2):
    Xs = StandardScaler().fit_transform(X)
    pca = PCA(n_components=n)
    return pca.fit_transform(Xs), pca
