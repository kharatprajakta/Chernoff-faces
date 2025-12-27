# Chernoff Faces

This repository demonstrates Chernoff faces — a way to visualize multivariate data by mapping variables to facial features. The included `chernoff.r` script shows examples using manual, simulated, and built-in datasets and saves example plots to the `plots/` folder.

**Highlights**
- Simple R script that uses the `aplpack` package to draw Chernoff faces.
- Example datasets: manual sample, simulated normal data, and the built-in `iris` dataset.
- Example PNG outputs saved to `plots/`.

**Requirements**
- R (tested on R 3.5+)
- The `aplpack` package

Install the required package from within R:

```r
install.packages("aplpack")
```

**Usage**

- Open the project in R and run the script interactively: open `chernoff.r` and run the examples.
- Or run from a shell using `Rscript`:

```bash
Rscript chernoff.r
```

Running the script will create a `plots/` directory (if missing) and write example PNG files such as `plots/chernoff_iris.png`, `plots/chernoff_data1.png`, and `plots/chernoff_plot.png`.

**What’s in this repository**
- Chernoff script: `chernoff.r` — examples and code to generate Chernoff faces.
- Output directory: `plots/` — generated example images (created when the script runs).
- License: see the `LICENSE` file.

**Examples**
- The script contains three examples:
	- A small manual data.frame sample.
	- A simulated dataset of 50 observations drawn from normal distributions.
	- The built-in `iris` dataset (using the first four numeric columns).

**Next steps / Tips**
- Edit or replace the example data frames in `chernoff.r` to visualize your own multivariate data.
- Map columns to facial features by reordering or scaling your variables prior to calling `faces()`.

