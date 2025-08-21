# Plot Style Template - Matplotlib

## Color

- Text: 'black'
- Plot Palette: `['#335A85','#4DA1A9','#D7E8BA','#FFB757','#F7713B','#611C35']`

## Font

Computer Modern Roman (LaTeX's default font)

## Font Size

- Chart Title: 30
- Axis Title: 28
- Other Text: 20

## Orientation/Location

- Chart Title: horizontal
- Vertical Axis Label: vertical
- Horizontal Axis Label: horizontal
- Tick Labels: horizontal

For the most part matplotlib defaults to this.

## Chart Elements

- For the most part do not add gridlines, unless it assists with reading the plot. If grid lines are included use color `#B1B1B1`.
- Keep the  horizontal and verical axis line, which is by default a solid black line. However, remove the upper and right axis line.
```
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
```
<!-- 
- If tick labels are numeric, keep the tick marks (default). For categorical axes, remove the tick marks. For example, if the x-axis is the categories for a bar chart, and the y-axis is the counts for the bars, then for the y-axis keep the default tick marks, but for the xaxis add the following code to remove the tick marks.
```
ax.xaxis.set_ticks_position('none')
``` -->

- Add a black border around bars in bar charts and histograms, and also around pie slices in pie charts. This is done by defining `edgecolor='black'` in the plotting function. Typically for scatter and line charts, the color of the border should match the color of the points/lines, which is the default.

## Legend

- No fill color for legend area `facecolor=None`
- Remove border around legend `framealpha=None, frameon=False`
- Position right of plot, can use `bbox_to_ancor` to specify location. The following sets it to the top right of plot `loc='upper left', bbox_to_anchor=(1.0, 1.0)`
- For bar charts, histograms, and pie charts set icons to be squares rather than rectangles `handlelength=0.5, handleheight=0.5`
- Typically you probably will want to reverse the order of the legend `reverse=True`

For bar charts, histograms, and pie charts the legend would be:
```
ax.legend(facecolor=None, framealpha=None, frameon=False,
          handlelength=0.5, handleheight=0.5, reverse=True,
          loc='upper left', bbox_to_anchor=(1.0, 1.0))
```

For scatter plots, line charts, and other charts the legend would be:
```
ax.legend(facecolor=None, framealpha=None, frameon=False, reverse=True,
          loc='upper left', bbox_to_anchor=(1.0, 1.0))
```