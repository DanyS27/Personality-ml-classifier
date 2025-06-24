def hist_plots(axes, x, xlabel, title=None):
    # Creating plot
    axes.hist(x)

    # Setting labels and title
    axes.set_xlabel(xlabel)
    axes.set_ylabel("# of observations")
    axes.set_title(title)
    
    # Marking mean and median
    axes.axvline(x.mean(), color="red", linestyle="--", label="mean")
    axes.axvline(x.median(), color="black", linestyle="--", label="median")
    axes.legend()
    
    # Grid
    axes.grid()